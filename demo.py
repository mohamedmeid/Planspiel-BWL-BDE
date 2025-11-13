"""
Demo-Skript für Factory Business Simulation
Führt automatisch ein Beispielspiel mit vordefinierten Entscheidungen durch
"""

from factory_simulator import FactorySimulator, GameParameters
import json


def run_demo_game():
    """Führe ein Demo-Spiel mit vordefinierten Strategien durch"""
    
    print("\n" + "="*70)
    print("FACTORY BUSINESS SIMULATION - DEMO")
    print("Planspiel BWL für BDE - WiSe 2025/26")
    print("="*70 + "\n")
    
    # Initialisiere Simulator
    params = GameParameters()
    simulator = FactorySimulator(params)
    
    print("Ausgangssituation:")
    print(f"  Kasse: {simulator.cash} M")
    print(f"  Forderungen: {simulator.accounts_receivable} M")
    print(f"  Lagerbestände: {simulator.raw_material_inventory} RM, "
          f"{simulator.work_in_progress} WIP, {simulator.finished_goods_inventory} FG\n")
    
    # Vordefinierte Strategien für 4 Szenarien
    scenarios = {
        "Szenario 1: Balanced": [
            {"sales_price": 13.0, "marketing": 1.0, "production": 2},
            {"sales_price": 13.5, "marketing": 1.0, "production": 2},
            {"sales_price": 13.0, "marketing": 1.5, "production": 2},
            {"sales_price": 13.5, "marketing": 0.5, "production": 2},
        ],
        "Szenario 2: Aggressive Pricing": [
            {"sales_price": 15.0, "marketing": 0.0, "production": 2},
            {"sales_price": 14.5, "marketing": 0.0, "production": 2},
            {"sales_price": 14.0, "marketing": 0.5, "production": 2},
            {"sales_price": 14.0, "marketing": 0.0, "production": 2},
        ],
        "Szenario 3: Marketing Focus": [
            {"sales_price": 13.0, "marketing": 2.0, "production": 3},
            {"sales_price": 13.0, "marketing": 2.5, "production": 3},
            {"sales_price": 13.0, "marketing": 2.0, "production": 3},
            {"sales_price": 13.5, "marketing": 1.0, "production": 2},
        ],
        "Szenario 4: Cost Leadership": [
            {"sales_price": 11.0, "marketing": 0.5, "production": 3},
            {"sales_price": 11.5, "marketing": 0.5, "production": 3},
            {"sales_price": 12.0, "marketing": 0.0, "production": 2},
            {"sales_price": 12.0, "marketing": 0.0, "production": 2},
        ],
    }
    
    # Wähle ein Szenario (oder führe alle durch)
    selected_scenario = "Szenario 1: Balanced"
    
    print(f"\n{'='*70}")
    print(f"Spiele: {selected_scenario}")
    print(f"{'='*70}\n")
    
    decisions = scenarios[selected_scenario]
    
    # Spiele 4 Quartale
    for quarter, decision in enumerate(decisions, 1):
        print(f"\n{'-'*70}")
        print(f"QUARTAL {quarter} - ENTSCHEIDUNGEN")
        print(f"{'-'*70}")
        print(f"  Verkaufspreis: {decision['sales_price']} M")
        print(f"  Marketing: {decision['marketing']} M")
        print(f"  Produktion: {decision['production']} Lose")
        
        # Simuliere Quartal
        result = simulator.simulate_quarter(
            sales_price=decision['sales_price'],
            marketing_budget=decision['marketing'],
            production_lots=decision['production']
        )
        
        # Zeige Ergebnisse
        print(f"\nERGEBNISSE:")
        print(f"  Nachfrage: {result.sales_volume} Lose")
        print(f"  Umsatz: {result.sales_revenue:.2f} M")
        print(f"  Kosten: {result.total_cost:.2f} M")
        print(f"  Gewinn: {result.net_profit:.2f} M")
        print(f"  Kasse: {result.cash_ending:.2f} M")
    
    # Zusammenfassung
    print(f"\n{'='*70}")
    print("JAHRESABSCHLUSS")
    print(f"{'='*70}")
    
    summary = simulator.get_summary()
    print(f"\nGESAMTERGEBNIS:")
    print(f"  Gesamtumsatz: {summary['total_revenue']:.2f} M")
    print(f"  Gesamtkosten: {summary['total_cost']:.2f} M")
    print(f"  Gesamtgewinn: {summary['total_profit']:.2f} M")
    print(f"  Ø Gewinn/Quartal: {summary['average_profit_per_quarter']:.2f} M")
    print(f"  Umsatzrendite: {summary['return_on_sales']:.2f}%")
    print(f"  Endbestand Kasse: {summary['final_cash']:.2f} M")
    
    # Bewertung
    print(f"\nBEWERTUNG:")
    profit = summary['total_profit']
    ros = summary['return_on_sales']
    
    if profit > 30 and ros > 20:
        rating = "AUSGEZEICHNET! 🌟"
        comment = "Hervorragende strategische Entscheidungen!"
    elif profit > 15 and ros > 10:
        rating = "GUT ✓"
        comment = "Solide Performance mit Verbesserungspotenzial."
    elif profit > 5 and ros > 5:
        rating = "BEFRIEDIGEND"
        comment = "Akzeptable Ergebnisse, aber deutliches Optimierungspotenzial."
    else:
        rating = "VERBESSERUNGSWÜRDIG"
        comment = "Strategie sollte überarbeitet werden."
    
    print(f"  {rating}")
    print(f"  {comment}")
    
    # Export
    filename = f"demo_{selected_scenario.replace(' ', '_').replace(':', '')}.json"
    simulator.export_results(filename)
    print(f"\nErgebnisse exportiert nach: {filename}")
    
    # Vergleichstabelle
    print(f"\n{'='*70}")
    print("QUARTALSÜBERSICHT")
    print(f"{'='*70}")
    print(f"{'Quartal':<10} {'Umsatz':<12} {'Kosten':<12} {'Gewinn':<12} {'Kasse':<12}")
    print(f"{'-'*70}")
    for result in simulator.results:
        print(f"Q{result.quarter:<9} {result.sales_revenue:<12.2f} {result.total_cost:<12.2f} "
              f"{result.net_profit:<12.2f} {result.cash_ending:<12.2f}")
    
    print("\n" + "="*70 + "\n")


def compare_all_scenarios():
    """Vergleiche alle Szenarien"""
    
    print("\n" + "="*70)
    print("SZENARIO-VERGLEICH")
    print("="*70 + "\n")
    
    scenarios = {
        "Balanced": [
            {"sales_price": 13.0, "marketing": 1.0, "production": 2},
            {"sales_price": 13.5, "marketing": 1.0, "production": 2},
            {"sales_price": 13.0, "marketing": 1.5, "production": 2},
            {"sales_price": 13.5, "marketing": 0.5, "production": 2},
        ],
        "Aggressive Pricing": [
            {"sales_price": 15.0, "marketing": 0.0, "production": 2},
            {"sales_price": 14.5, "marketing": 0.0, "production": 2},
            {"sales_price": 14.0, "marketing": 0.5, "production": 2},
            {"sales_price": 14.0, "marketing": 0.0, "production": 2},
        ],
        "Marketing Focus": [
            {"sales_price": 13.0, "marketing": 2.0, "production": 3},
            {"sales_price": 13.0, "marketing": 2.5, "production": 3},
            {"sales_price": 13.0, "marketing": 2.0, "production": 3},
            {"sales_price": 13.5, "marketing": 1.0, "production": 2},
        ],
        "Cost Leadership": [
            {"sales_price": 11.0, "marketing": 0.5, "production": 3},
            {"sales_price": 11.5, "marketing": 0.5, "production": 3},
            {"sales_price": 12.0, "marketing": 0.0, "production": 2},
            {"sales_price": 12.0, "marketing": 0.0, "production": 2},
        ],
    }
    
    results_comparison = {}
    
    for scenario_name, decisions in scenarios.items():
        print(f"Spiele Szenario: {scenario_name}...")
        simulator = FactorySimulator()
        
        for decision in decisions:
            simulator.simulate_quarter(
                sales_price=decision['sales_price'],
                marketing_budget=decision['marketing'],
                production_lots=decision['production']
            )
        
        summary = simulator.get_summary()
        results_comparison[scenario_name] = summary
    
    # Ausgabe der Vergleichstabelle
    print(f"\n{'='*100}")
    print(f"{'Szenario':<25} {'Umsatz':<15} {'Kosten':<15} {'Gewinn':<15} {'ROS %':<12} {'Kasse':<12}")
    print(f"{'='*100}")
    
    for scenario, summary in results_comparison.items():
        print(f"{scenario:<25} {summary['total_revenue']:<15.2f} {summary['total_cost']:<15.2f} "
              f"{summary['total_profit']:<15.2f} {summary['return_on_sales']:<12.2f} "
              f"{summary['final_cash']:<12.2f}")
    
    # Gewinner ermitteln
    best_scenario = max(results_comparison.items(), key=lambda x: x[1]['total_profit'])
    print(f"\n{'='*100}")
    print(f"BESTES SZENARIO: {best_scenario[0]}")
    print(f"Gesamtgewinn: {best_scenario[1]['total_profit']:.2f} M")
    print(f"{'='*100}\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--compare":
        compare_all_scenarios()
    else:
        run_demo_game()
        
        print("\nTipp: Führe 'python3 demo.py --compare' aus, um alle Szenarien zu vergleichen!")
