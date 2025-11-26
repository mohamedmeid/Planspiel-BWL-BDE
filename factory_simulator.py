"""
Factory Business Simulation Game - Enhanced Interactive Version
Planspiel BWL für BDE - WiSe 2025/26
Ostfalia Hochschule für angewandte Wissenschaften

This module implements an enhanced version of the Factory game with:
- Variable sales prices
- Variable production costs
- Variable purchase prices
- Variable overhead costs
- Marketing investment options
- Abschreibungen (Depreciation)
- Zinsen (Interest)
- Steuern (Taxes)
"""

import json
from typing import Dict, List
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class GameParameters:
    """Configuration parameters for the Factory game"""
    # Base prices (can be modified)
    base_sales_price: float = 13.0  # Per unit
    base_material_price: float = 3.0  # Per lot
    base_production_cost: float = 3.0  # Per lot (Fertigungsstufe 1)
    base_assembly_cost: float = 1.0  # Per lot (Fertigungsstufe 2)
    base_overhead_cost: float = 6.0  # Per quarter
    
    # Financial parameters (from original Factory game)
    depreciation_per_quarter: float = 2.25  # 9M per year / 4 quarters
    interest_per_quarter: float = 2.5  # 10M per year / 4 quarters
    tax_rate: float = 0.3333  # 33.33% (1/3 of profit before tax)
    credit_volume: float = 100.0  # Total credit
    interest_rate: float = 0.10  # 10% annual interest rate
    
    # Variable factors
    marketing_budget: float = 0.0  # Additional marketing spend
    price_elasticity: float = 0.15  # Sales volume change per 1% price change
    marketing_effectiveness: float = 0.08  # Sales increase per M invested
    
    # Market conditions
    market_demand_base: int = 2  # Base lots per quarter
    competitor_price: float = 12.5  # Competitor pricing
    
    # Production efficiency
    production_efficiency: float = 1.0  # 1.0 = normal, 0.9 = 10% cost reduction
    quality_factor: float = 1.0  # Affects production costs


@dataclass
class QuarterResult:
    """Results for a single quarter"""
    quarter: int
    
    # Player decisions
    material_purchase_lots: int
    production_lots: int
    
    # Sales data
    sales_price: float
    sales_volume: int
    sales_revenue: float
    
    # Costs
    material_cost: float
    production_cost: float
    assembly_cost: float
    herstellungskosten: float  # Total manufacturing costs (Material + Production + Assembly)
    overhead_cost: float  # Gemeinkosten
    marketing_cost: float
    depreciation: float  # Abschreibungen
    interest: float  # Zinsen
    total_operating_cost: float  # All costs before interest
    
    # Results according to GuV structure
    gross_profit: float  # Bruttoergebnis = Revenue - Herstellungskosten
    ebit: float  # Betriebsergebnis = Gross Profit - Overhead - Depreciation
    profit_before_tax: float  # Gewinn vor Steuern = EBIT - Interest
    tax: float  # Steuern
    net_profit: float  # Gewinn nach Steuern
    
    # Inventory
    raw_material_inventory: int
    work_in_progress: int
    finished_goods_inventory: int
    
    # Cash flow
    cash_beginning: float
    cash_ending: float
    accounts_receivable: float


class FactorySimulator:
    """Main simulation engine for the Factory game"""
    
    def __init__(self, parameters: GameParameters = None):
        self.params = parameters or GameParameters()
        self.current_quarter = 0
        self.results: List[QuarterResult] = []
        
        # Initial state (from original game)
        self.cash = 28.0  # Initial M (Münzen)
        self.accounts_receivable = 26.0
        self.raw_material_inventory = 2  # Lots
        self.work_in_progress = 2  # Lots
        self.finished_goods_inventory = 2  # Lots
        
        # Annual totals for year-end reporting
        self.annual_depreciation = 0.0
        self.annual_interest = 0.0
        self.annual_tax = 0.0
    
    def calculate_demand(self, sales_price: float, marketing_spend: float) -> int:
        """
        Calculate sales volume based on price and marketing
        
        Formula:
        - Base demand modified by price elasticity
        - Marketing investment increases demand
        - Competitor pricing affects demand
        """
        # Price effect on demand
        price_ratio = sales_price / self.params.base_sales_price
        price_effect = 1.0 - (price_ratio - 1.0) * self.params.price_elasticity
        
        # Marketing effect on demand
        marketing_effect = 1.0 + (marketing_spend * self.params.marketing_effectiveness)
        
        # Competitive effect
        if sales_price > self.params.competitor_price:
            competitive_penalty = 0.85
        elif sales_price < self.params.competitor_price:
            competitive_penalty = 1.15
        else:
            competitive_penalty = 1.0
        
        # Calculate total demand
        demand = self.params.market_demand_base * price_effect * marketing_effect * competitive_penalty
        
        return max(1, round(demand))  # At least 1 lot
    
    def calculate_production_cost(self, lots: int) -> float:
        """Calculate production costs with efficiency factors"""
        base_cost = lots * self.params.base_production_cost
        adjusted_cost = base_cost * self.params.production_efficiency * self.params.quality_factor
        return round(adjusted_cost, 2)
    
    def calculate_material_cost(self, lots: int, market_factor: float = 1.0) -> float:
        """Calculate material costs with market fluctuations"""
        return round(lots * self.params.base_material_price * market_factor, 2)
    
    def simulate_quarter(self, 
                        sales_price: float = None,
                        marketing_budget: float = 0.0,
                        production_lots: int = 2,
                        material_purchase_lots: int = 2,
                        material_market_factor: float = 1.0,
                        overhead_factor: float = 1.0) -> QuarterResult:
        """
        Simulate one quarter with given decisions
        
        Args:
            sales_price: Selling price per unit (if None, uses base price)
            marketing_budget: Additional marketing spend
            production_lots: Number of lots to produce
            material_purchase_lots: Number of material lots to order
            material_market_factor: Material price multiplier (e.g., 1.1 = 10% increase)
            overhead_factor: Overhead cost multiplier
        """
        self.current_quarter += 1
        cash_beginning = self.cash
        
        # Use base price if not specified
        if sales_price is None:
            sales_price = self.params.base_sales_price
        
        # Calculate demand based on price and marketing
        sales_volume = self.calculate_demand(sales_price, marketing_budget)
        sales_volume = min(sales_volume, self.finished_goods_inventory)  # Can't sell more than inventory
        
        # Calculate revenues (Umsatzerlöse)
        sales_revenue = sales_volume * sales_price
        
        # Calculate costs
        material_cost = self.calculate_material_cost(material_purchase_lots, material_market_factor)
        production_cost = self.calculate_production_cost(production_lots)
        assembly_cost = production_lots * self.params.base_assembly_cost
        
        # Herstellungskosten = Material + Production + Assembly (for goods sold)
        # Note: In the original game, this represents costs of goods sold
        herstellungskosten = material_cost + production_cost + assembly_cost
        
        # Gemeinkosten (Overhead)
        overhead_cost = self.params.base_overhead_cost * overhead_factor
        marketing_cost = marketing_budget
        
        # Abschreibungen (Depreciation) - NO CASH OUTFLOW
        depreciation = self.params.depreciation_per_quarter
        self.annual_depreciation += depreciation
        
        # Calculate GuV structure
        # Bruttoergebnis = Umsatz - Herstellungskosten
        gross_profit = sales_revenue - herstellungskosten
        
        # Betriebsergebnis (EBIT) = Bruttoergebnis - Gemeinkosten - Abschreibungen
        ebit = gross_profit - overhead_cost - depreciation
        
        # Zinsen (Interest) - CASH OUTFLOW
        interest = self.params.interest_per_quarter
        self.annual_interest += interest
        
        # Gewinn vor Steuern = EBIT - Zinsen
        profit_before_tax = ebit - interest
        
        # Steuern (Taxes) = 33.33% of profit before tax (only if profit > 0)
        tax = max(0, profit_before_tax * self.params.tax_rate)
        self.annual_tax += tax
        
        # Gewinn nach Steuern (Net Profit)
        net_profit = profit_before_tax - tax
        
        # Total operating costs (for cash flow calculation)
        # Cash outflows: Material, Production, Assembly, Overhead, Marketing, Interest, Tax
        # NOT Depreciation (no cash flow)
        total_cash_costs = (material_cost + production_cost + assembly_cost + 
                           overhead_cost + marketing_cost + interest + tax)
        
        # Update inventory
        # Material: receive order, consume for production
        self.raw_material_inventory += material_purchase_lots
        self.raw_material_inventory -= production_lots
        
        # WIP: produced - assembled
        self.work_in_progress += production_lots
        self.work_in_progress -= production_lots  # Moved to finished goods
        
        # Finished goods: assembled - sold
        self.finished_goods_inventory += production_lots
        self.finished_goods_inventory -= sales_volume
        
        # Update cash flow
        # Cash in: customer payments (previous quarter receivables)
        cash_in = self.accounts_receivable
        self.cash += cash_in
        
        # Cash out: all costs that involve actual cash payments
        self.cash -= total_cash_costs
        
        # New receivables from this quarter's sales
        self.accounts_receivable = sales_revenue
        
        cash_ending = self.cash
        
        # Create quarter result
        result = QuarterResult(
            quarter=self.current_quarter,
            material_purchase_lots=material_purchase_lots,
            production_lots=production_lots,
            sales_price=sales_price,
            sales_volume=sales_volume,
            sales_revenue=sales_revenue,
            material_cost=material_cost,
            production_cost=production_cost,
            assembly_cost=assembly_cost,
            herstellungskosten=herstellungskosten,
            overhead_cost=overhead_cost,
            marketing_cost=marketing_cost,
            depreciation=depreciation,
            interest=interest,
            total_operating_cost=total_cash_costs,
            gross_profit=gross_profit,
            ebit=ebit,
            profit_before_tax=profit_before_tax,
            tax=tax,
            net_profit=net_profit,
            raw_material_inventory=self.raw_material_inventory,
            work_in_progress=self.work_in_progress,
            finished_goods_inventory=self.finished_goods_inventory,
            cash_beginning=cash_beginning,
            cash_ending=cash_ending,
            accounts_receivable=self.accounts_receivable
        )
        
        self.results.append(result)
        return result
    
    def get_summary(self) -> Dict:
        """Get summary of all quarters"""
        if not self.results:
            return {}
        
        total_revenue = sum(r.sales_revenue for r in self.results)
        total_herstellungskosten = sum(r.herstellungskosten for r in self.results)
        total_overhead = sum(r.overhead_cost for r in self.results)
        total_marketing = sum(r.marketing_cost for r in self.results)
        total_depreciation = sum(r.depreciation for r in self.results)
        total_interest = sum(r.interest for r in self.results)
        total_tax = sum(r.tax for r in self.results)
        total_net_profit = sum(r.net_profit for r in self.results)
        total_ebit = sum(r.ebit for r in self.results)
        total_gross_profit = sum(r.gross_profit for r in self.results)
        
        return {
            "quarters_played": len(self.results),
            "total_revenue": round(total_revenue, 2),
            "total_herstellungskosten": round(total_herstellungskosten, 2),
            "total_gross_profit": round(total_gross_profit, 2),
            "total_overhead": round(total_overhead, 2),
            "total_marketing": round(total_marketing, 2),
            "total_depreciation": round(total_depreciation, 2),
            "total_ebit": round(total_ebit, 2),
            "total_interest": round(total_interest, 2),
            "total_profit_before_tax": round(total_ebit - total_interest, 2),
            "total_tax": round(total_tax, 2),
            "total_net_profit": round(total_net_profit, 2),
            "average_profit_per_quarter": round(total_net_profit / len(self.results), 2),
            "final_cash": round(self.cash, 2),
            "return_on_sales": round((total_net_profit / total_revenue * 100) if total_revenue > 0 else 0, 2)
        }
    
    def export_results(self, filename: str = "factory_results.json"):
        """Export results to JSON file"""
        data = {
            "parameters": asdict(self.params),
            "quarters": [asdict(r) for r in self.results],
            "summary": self.get_summary()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return filename
    
    def print_quarter_report(self, result: QuarterResult):
        """Print formatted quarter report with GuV structure"""
        print(f"\n{'='*60}")
        print(f"QUARTAL {result.quarter} - GEWINN- UND VERLUSTRECHNUNG")
        print(f"{'='*60}")
        
        print(f"\nUmsatzerlöse:              {result.sales_revenue:>8.2f} M")
        print(f"  (Verkaufspreis: {result.sales_price:.2f} M × {result.sales_volume} Lose)")
        
        print(f"\nHerstellungskosten:        {result.herstellungskosten:>8.2f} M")
        print(f"  Material:                {result.material_cost:>8.2f} M")
        print(f"  Fertigung:               {result.production_cost:>8.2f} M")
        print(f"  Montage:                 {result.assembly_cost:>8.2f} M")
        
        print(f"\n= Bruttoergebnis:          {result.gross_profit:>8.2f} M")
        
        print(f"\nGemeinkosten:              {result.overhead_cost:>8.2f} M")
        print(f"Marketing:                 {result.marketing_cost:>8.2f} M")
        print(f"Abschreibungen:            {result.depreciation:>8.2f} M")
        
        print(f"\n= Betriebsergebnis (EBIT): {result.ebit:>8.2f} M")
        
        print(f"\nZinsen:                    {result.interest:>8.2f} M")
        
        print(f"\n= Gewinn vor Steuern:      {result.profit_before_tax:>8.2f} M")
        
        print(f"\nSteuern (33.33%):          {result.tax:>8.2f} M")
        
        print(f"\n{'='*60}")
        print(f"= GEWINN NACH STEUERN:     {result.net_profit:>8.2f} M")
        print(f"{'='*60}")
        
        print(f"\nBESTÄNDE:")
        print(f"  Rohmaterial:             {result.raw_material_inventory:>8} Los(e)")
        print(f"  Halbfertigprodukte:      {result.work_in_progress:>8} Los(e)")
        print(f"  Fertigprodukte:          {result.finished_goods_inventory:>8} Los(e)")
        
        print(f"\nLIQUIDITÄT:")
        print(f"  Kasse Anfang:            {result.cash_beginning:>8.2f} M")
        print(f"  Kasse Ende:              {result.cash_ending:>8.2f} M")
        print(f"  Forderungen:             {result.accounts_receivable:>8.2f} M")
        print(f"{'='*60}\n")


def run_interactive_game():
    """Run interactive game session"""
    print("\n" + "="*60)
    print("FACTORY BUSINESS SIMULATION - INTERAKTIVE VERSION")
    print("mit Abschreibungen, Zinsen und Steuern")
    print("Planspiel BWL für BDE - WiSe 2025/26")
    print("="*60 + "\n")
    
    # Initialize game
    params = GameParameters()
    simulator = FactorySimulator(params)
    
    print("Startzustand:")
    print(f"  Kasse: {simulator.cash} M")
    print(f"  Forderungen: {simulator.accounts_receivable} M")
    print(f"  Rohmaterial: {simulator.raw_material_inventory} Los(e)")
    print(f"  Halbfertig: {simulator.work_in_progress} Los(e)")
    print(f"  Fertigprodukte: {simulator.finished_goods_inventory} Los(e)")
    print(f"\nFinanzielle Parameter:")
    print(f"  Abschreibung pro Quartal: {params.depreciation_per_quarter} M")
    print(f"  Zinsen pro Quartal: {params.interest_per_quarter} M")
    print(f"  Steuersatz: {params.tax_rate*100:.1f}%")
    
    # Play 4 quarters
    for quarter in range(1, 5):
        print(f"\n{'='*60}")
        print(f"QUARTAL {quarter} - ENTSCHEIDUNGEN")
        print(f"{'='*60}")
        
        # Get user decisions
        try:
            sales_price = float(input(f"Verkaufspreis (Standard: {params.base_sales_price} M): ") or params.base_sales_price)
            marketing = float(input("Marketing-Budget (Standard: 0 M): ") or 0)
            production = int(input("Produktionsmenge in Los (Standard: 2): ") or 2)
            material = int(input("Materialeinkauf in Los (Standard: 2): ") or 2)
            
            # Simulate quarter
            result = simulator.simulate_quarter(
                sales_price=sales_price,
                marketing_budget=marketing,
                production_lots=production,
                material_purchase_lots=material
            )
            
            # Show results
            simulator.print_quarter_report(result)
            
        except ValueError:
            print("Ungültige Eingabe! Verwende Standardwerte.")
            result = simulator.simulate_quarter()
            simulator.print_quarter_report(result)
    
    # Final summary
    print("\n" + "="*60)
    print("JAHRESABSCHLUSS - ZUSAMMENFASSUNG")
    print("="*60)
    summary = simulator.get_summary()
    
    print(f"\nGUV - GESAMT:")
    print(f"  Umsatzerlöse:                    {summary['total_revenue']:>10.2f} M")
    print(f"  Herstellungskosten:              {summary['total_herstellungskosten']:>10.2f} M")
    print(f"  = Bruttoergebnis:                {summary['total_gross_profit']:>10.2f} M")
    print(f"  Gemeinkosten:                    {summary['total_overhead']:>10.2f} M")
    print(f"  Marketing:                       {summary['total_marketing']:>10.2f} M")
    print(f"  Abschreibungen:                  {summary['total_depreciation']:>10.2f} M")
    print(f"  = Betriebsergebnis (EBIT):       {summary['total_ebit']:>10.2f} M")
    print(f"  Zinsen:                          {summary['total_interest']:>10.2f} M")
    print(f"  = Gewinn vor Steuern:            {summary['total_profit_before_tax']:>10.2f} M")
    print(f"  Steuern:                         {summary['total_tax']:>10.2f} M")
    print(f"  = GEWINN NACH STEUERN:           {summary['total_net_profit']:>10.2f} M")
    
    print(f"\nKENNZAHLEN:")
    print(f"  Ø Gewinn pro Quartal:            {summary['average_profit_per_quarter']:>10.2f} M")
    print(f"  Umsatzrendite:                   {summary['return_on_sales']:>10.2f}%")
    print(f"  Endbestand Kasse:                {summary['final_cash']:>10.2f} M")
    
    # Export results
    filename = simulator.export_results()
    print(f"\nErgebnisse exportiert nach: {filename}")


if __name__ == "__main__":
    run_interactive_game()
