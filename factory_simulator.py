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
"""

import json
from typing import Dict, List, Tuple
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
    overhead_cost: float
    marketing_cost: float
    total_cost: float

    # Results
    gross_profit: float
    net_profit: float

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
        
        # Production pipeline for WIP delay
        # Stores production lots that will enter WIP in the next quarter
        self.production_pipeline = 0

        # Orders pending (from original game setup)
        self.pending_orders = [
            {"quarter": 1, "volume": 2, "price": 13.0},
            {"quarter": 2, "volume": 2, "price": 12.5},
            {"quarter": 3, "volume": 2, "price": 12.5},
            {"quarter": 4, "volume": 2, "price": 13.0}
        ]
    
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
            production_lots: Number of lots to produce (starts production)
            material_purchase_lots: Number of raw material lots to buy
            material_market_factor: Material price multiplier (e.g., 1.1 = 10% increase)
            overhead_factor: Overhead cost multiplier
        """
        self.current_quarter += 1
        cash_beginning = self.cash
        
        # Use base price if not specified
        if sales_price is None:
            sales_price = self.params.base_sales_price
        
        # --- 1. Material Purchase & Consumption ---
        # Buy materials
        self.raw_material_inventory += material_purchase_lots
        material_cost = self.calculate_material_cost(material_purchase_lots, material_market_factor)
        
        # Check if we have enough material for production
        # If not, reduce production to match available material
        if self.raw_material_inventory < production_lots:
            # Could log a warning here
            production_lots = self.raw_material_inventory
            
        # Consume materials for NEW production
        self.raw_material_inventory -= production_lots
        
        # --- 2. Production (WIP Flow) ---
        # Logic: 
        # - New production enters the 'pipeline' (takes time to start/process)
        # - Items from the 'pipeline' (started last quarter) move to WIP? 
        # - OR: Simple flow: Raw -> WIP (1 qtr) -> Finished (1 qtr)
        # Let's stick to a simpler reliable flow for this game scale:
        # Current Production adds to WIP immediately, but WIP -> Finished happens from *existing* WIP.
        # To simulate flow: 
        #   Start of Q: We have WIP from previous Q.
        #   We finish the WIP -> moves to Finished Goods.
        #   We start NEW production -> moves from Raw to WIP.
        
        # Step A: Finish existing WIP
        lots_finished = self.work_in_progress
        self.finished_goods_inventory += lots_finished
        self.work_in_progress -= lots_finished
        
        # Step B: Start new production (moves to WIP)
        self.work_in_progress += production_lots
        
        # Costs associated with the activities
        production_cost = self.calculate_production_cost(production_lots) # Cost of STARTING production
        assembly_cost = lots_finished * self.params.base_assembly_cost # Cost of FINISHING goods
        
        # --- 3. Sales ---
        # Calculate demand
        sales_volume = self.calculate_demand(sales_price, marketing_budget)
        
        # Limit sales to available finished goods
        sales_volume = min(sales_volume, self.finished_goods_inventory)
        
        # Remove sold goods
        self.finished_goods_inventory -= sales_volume
        
        # --- 4. Financials ---
        sales_revenue = sales_volume * sales_price
        
        overhead_cost = self.params.base_overhead_cost * overhead_factor
        marketing_cost = marketing_budget
        
        total_cost = material_cost + production_cost + assembly_cost + overhead_cost + marketing_cost
        
        # Gross profit (Revenue - Direct Costs)
        # Note: This is a simplified cash-basis calculation for the game, not strict accrual accounting
        gross_profit = sales_revenue - (material_cost + production_cost + assembly_cost)
        net_profit = sales_revenue - total_cost
        
        # Cash Flow
        # In: Receivables from PREVIOUS quarter
        cash_in = self.accounts_receivable
        self.cash += cash_in
        
        # Out: All current costs
        self.cash -= total_cost
        
        # New Receivables: This quarter's revenue (paid next quarter)
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
            overhead_cost=overhead_cost,
            marketing_cost=marketing_cost,
            total_cost=total_cost,
            gross_profit=gross_profit,
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
        total_cost = sum(r.total_cost for r in self.results)
        total_profit = sum(r.net_profit for r in self.results)
        
        return {
            "quarters_played": len(self.results),
            "total_revenue": round(total_revenue, 2),
            "total_cost": round(total_cost, 2),
            "total_profit": round(total_profit, 2),
            "average_profit_per_quarter": round(total_profit / len(self.results), 2),
            "final_cash": round(self.cash, 2),
            "return_on_sales": round((total_profit / total_revenue * 100) if total_revenue > 0 else 0, 2)
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
        """Print formatted quarter report"""
        print(f"\n{'='*60}")
        print(f"QUARTAL {result.quarter} - ERGEBNISBERICHT")
        print(f"{'='*60}")
        print(f"\nVERKAUF:")
        print(f"  Verkaufspreis:        {result.sales_price:>8.2f} M/Einheit")
        print(f"  Absatzmenge:          {result.sales_volume:>8} Los(e)")
        print(f"  Umsatz:               {result.sales_revenue:>8.2f} M")
        
        print(f"\nKOSTEN:")
        print(f"  Materialkosten:       {result.material_cost:>8.2f} M")
        print(f"  Fertigungskosten:     {result.production_cost:>8.2f} M")
        print(f"  Montagekosten:        {result.assembly_cost:>8.2f} M")
        print(f"  Gemeinkosten:         {result.overhead_cost:>8.2f} M")
        print(f"  Marketingkosten:      {result.marketing_cost:>8.2f} M")
        print(f"  Gesamtkosten:         {result.total_cost:>8.2f} M")
        
        print(f"\nERGEBNIS:")
        print(f"  Bruttogewinn:         {result.gross_profit:>8.2f} M")
        print(f"  Nettogewinn:          {result.net_profit:>8.2f} M")
        
        print(f"\nBESTÄNDE:")
        print(f"  Rohmaterial:          {result.raw_material_inventory:>8} Los(e)")
        print(f"  Halbfertigprodukte:   {result.work_in_progress:>8} Los(e)")
        print(f"  Fertigprodukte:       {result.finished_goods_inventory:>8} Los(e)")
        
        print(f"\nLIQUIDITÄT:")
        print(f"  Kasse Anfang:         {result.cash_beginning:>8.2f} M")
        print(f"  Kasse Ende:           {result.cash_ending:>8.2f} M")
        print(f"  Forderungen:          {result.accounts_receivable:>8.2f} M")
        print(f"{'='*60}\n")


def run_interactive_game():
    """Run interactive game session"""
    print("\n" + "="*60)
    print("FACTORY BUSINESS SIMULATION - INTERAKTIVE VERSION")
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
            
            # Simulate quarter
            result = simulator.simulate_quarter(
                sales_price=sales_price,
                marketing_budget=marketing,
                production_lots=production
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
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    # Export results
    filename = simulator.export_results()
    print(f"\nErgebnisse exportiert nach: {filename}")


if __name__ == "__main__":
    run_interactive_game()
