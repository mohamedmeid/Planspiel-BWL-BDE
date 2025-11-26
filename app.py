"""
Flask Web Application for Factory Business Simulation
Provides web-based interface for the game
"""

from flask import Flask, render_template, request, jsonify, session, send_file
import json
import os
from datetime import datetime
from factory_simulator import FactorySimulator, GameParameters, QuarterResult
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

app = Flask(__name__)
app.secret_key = 'factory_simulation_secret_key_2025'

# Store simulators in memory (in production, use database)
simulators = {}


@app.route('/')
def index():
    """Main game interface"""
    return render_template('index.html')


@app.route('/api/start_game', methods=['POST'])
def start_game():
    """Initialize a new game"""
    data = request.json
    
    # Create game parameters
    params = GameParameters(
        base_sales_price=float(data.get('base_sales_price', 13.0)),
        base_material_price=float(data.get('base_material_price', 3.0)),
        base_production_cost=float(data.get('base_production_cost', 3.0)),
        base_assembly_cost=float(data.get('base_assembly_cost', 1.0)),
        base_overhead_cost=float(data.get('base_overhead_cost', 6.0))
    )
    
    # Create simulator
    game_id = data.get('game_id', 'default')
    simulator = FactorySimulator(params)
    simulators[game_id] = simulator
    
    return jsonify({
        'success': True,
        'game_id': game_id,
        'initial_state': {
            'cash': simulator.cash,
            'accounts_receivable': simulator.accounts_receivable,
            'raw_material_inventory': simulator.raw_material_inventory,
            'work_in_progress': simulator.work_in_progress,
            'finished_goods_inventory': simulator.finished_goods_inventory
        }
    })


@app.route('/api/simulate_quarter', methods=['POST'])
def simulate_quarter():
    """Simulate one quarter with given decisions"""
    data = request.json
    game_id = data.get('game_id', 'default')
    
    if game_id not in simulators:
        return jsonify({'success': False, 'error': 'Game not found'}), 404
    
    simulator = simulators[game_id]
    
    # Extract decisions
    sales_price = float(data.get('sales_price', 13.0))
    marketing_budget = float(data.get('marketing_budget', 0))
    production_lots = int(data.get('production_lots', 2))
    material_purchase_lots = int(data.get('material_purchase_lots', 2))
    material_market_factor = float(data.get('material_market_factor', 1.0))
    overhead_factor = float(data.get('overhead_factor', 1.0))
    
    # Run simulation
    result = simulator.simulate_quarter(
        sales_price=sales_price,
        marketing_budget=marketing_budget,
        production_lots=production_lots,
        material_purchase_lots=material_purchase_lots,
        material_market_factor=material_market_factor,
        overhead_factor=overhead_factor
    )
    
    # Convert result to dict
    result_dict = {
        'quarter': result.quarter,
        'material_purchase_lots': result.material_purchase_lots,
        'production_lots': result.production_lots,
        'sales_price': result.sales_price,
        'sales_volume': result.sales_volume,
        'sales_revenue': result.sales_revenue,
        'material_cost': result.material_cost,
        'production_cost': result.production_cost,
        'assembly_cost': result.assembly_cost,
        'overhead_cost': result.overhead_cost,
        'marketing_cost': result.marketing_cost,
        'total_cost': result.total_cost,
        'gross_profit': result.gross_profit,
        'net_profit': result.net_profit,
        'raw_material_inventory': result.raw_material_inventory,
        'work_in_progress': result.work_in_progress,
        'finished_goods_inventory': result.finished_goods_inventory,
        'cash_beginning': result.cash_beginning,
        'cash_ending': result.cash_ending,
        'accounts_receivable': result.accounts_receivable
    }
    
    return jsonify({
        'success': True,
        'result': result_dict,
        'current_state': {
            'cash': simulator.cash,
            'accounts_receivable': simulator.accounts_receivable,
            'raw_material_inventory': simulator.raw_material_inventory,
            'work_in_progress': simulator.work_in_progress,
            'finished_goods_inventory': simulator.finished_goods_inventory
        }
    })


@app.route('/api/get_summary', methods=['GET'])
def get_summary():
    """Get game summary"""
    game_id = request.args.get('game_id', 'default')
    
    if game_id not in simulators:
        return jsonify({'success': False, 'error': 'Game not found'}), 404
    
    simulator = simulators[game_id]
    summary = simulator.get_summary()
    
    return jsonify({
        'success': True,
        'summary': summary,
        'results': [
            {
                'quarter': r.quarter,
                'sales_revenue': r.sales_revenue,
                'total_cost': r.total_cost,
                'net_profit': r.net_profit,
                'cash_ending': r.cash_ending
            }
            for r in simulator.results
        ]
    })


@app.route('/api/export_results', methods=['GET'])
def export_results():
    """Export game results as JSON"""
    game_id = request.args.get('game_id', 'default')

    if game_id not in simulators:
        return jsonify({'success': False, 'error': 'Game not found'}), 404

    simulator = simulators[game_id]
    filename = f"factory_results_{game_id}.json"
    simulator.export_results(filename)

    return jsonify({
        'success': True,
        'filename': filename,
        'message': 'Results exported successfully'
    })


@app.route('/api/export_excel', methods=['GET'])
def export_excel():
    """Export game results as Excel file"""
    game_id = request.args.get('game_id', 'default')

    if game_id not in simulators:
        return jsonify({'success': False, 'error': 'Game not found'}), 404

    simulator = simulators[game_id]
    summary = simulator.get_summary()

    # Create workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Spielergebnisse"

    # Styling
    header_fill = PatternFill(start_color="667eea", end_color="667eea", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=12)
    title_font = Font(bold=True, size=16, color="2d3748")
    subtitle_font = Font(size=11, color="718096")

    positive_fill = PatternFill(start_color="c6f6d5", end_color="c6f6d5", fill_type="solid")
    negative_fill = PatternFill(start_color="fed7d7", end_color="fed7d7", fill_type="solid")

    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    # Title section
    ws.merge_cells('A1:H1')
    ws['A1'] = "🏭 Factory Business Simulation - Spielergebnisse"
    ws['A1'].font = title_font
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')

    ws.merge_cells('A2:H2')
    ws['A2'] = f"Planspiel BWL für BDE - WiSe 2025/26"
    ws['A2'].font = subtitle_font
    ws['A2'].alignment = Alignment(horizontal='center')

    ws.merge_cells('A3:H3')
    ws['A3'] = "Ostfalia Hochschule für angewandte Wissenschaften"
    ws['A3'].font = subtitle_font
    ws['A3'].alignment = Alignment(horizontal='center')

    ws.merge_cells('A4:H4')
    ws['A4'] = f"Erstellt am: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
    ws['A4'].font = subtitle_font
    ws['A4'].alignment = Alignment(horizontal='center')

    # Summary section
    row = 6
    ws.merge_cells(f'A{row}:H{row}')
    ws[f'A{row}'] = "📊 Jahresabschluss"
    ws[f'A{row}'].font = Font(bold=True, size=14, color="667eea")

    row += 2
    summary_data = [
        ['Gesamtumsatz', f"{summary['total_revenue']:.2f} M", 'positive'],
        ['Gesamtkosten', f"{summary['total_cost']:.2f} M", 'negative'],
        ['Gesamtgewinn', f"{summary['total_profit']:.2f} M", 'profit'],
        ['Durchschnittlicher Gewinn pro Quartal', f"{summary['average_profit_per_quarter']:.2f} M", ''],
        ['Endbestand Kasse', f"{summary['final_cash']:.2f} M", 'positive'],
        ['Umsatzrendite', f"{summary['return_on_sales']:.2f}%", ''],
    ]

    for label, value, style in summary_data:
        ws[f'B{row}'] = label
        ws[f'B{row}'].font = Font(bold=True)
        ws[f'D{row}'] = value
        ws[f'D{row}'].font = Font(bold=True, size=12)

        if style == 'positive':
            ws[f'D{row}'].fill = positive_fill
            ws[f'D{row}'].font = Font(bold=True, size=12, color="22543d")
        elif style == 'negative':
            ws[f'D{row}'].fill = negative_fill
            ws[f'D{row}'].font = Font(bold=True, size=12, color="742a2a")
        elif style == 'profit':
            if summary['total_profit'] >= 0:
                ws[f'D{row}'].fill = positive_fill
                ws[f'D{row}'].font = Font(bold=True, size=12, color="22543d")
            else:
                ws[f'D{row}'].fill = negative_fill
                ws[f'D{row}'].font = Font(bold=True, size=12, color="742a2a")

        row += 1

    # Player Decisions section
    row += 2
    ws.merge_cells(f'A{row}:H{row}')
    ws[f'A{row}'] = "🎯 Spieler Entscheidungen"
    ws[f'A{row}'].font = Font(bold=True, size=14, color="667eea")

    row += 2
    decision_headers = ['Quartal', 'Rohmaterial Einkauf', 'Produktion', 'Verkaufspreis', 'Marketing']
    for col, header in enumerate(decision_headers, start=1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = border

    row += 1
    for result in simulator.results:
        ws.cell(row=row, column=1, value=f"Q{result.quarter}")
        ws.cell(row=row, column=2, value=f"{result.material_purchase_lots} Lose")
        ws.cell(row=row, column=3, value=f"{result.production_lots} Lose")
        ws.cell(row=row, column=4, value=f"{result.sales_price:.2f} M")
        ws.cell(row=row, column=5, value=f"{result.marketing_cost:.2f} M")

        # Apply borders
        for col in range(1, 6):
            ws.cell(row=row, column=col).border = border
            ws.cell(row=row, column=col).alignment = Alignment(horizontal='center')

        row += 1

    # Quarterly results section
    row += 2
    ws.merge_cells(f'A{row}:H{row}')
    ws[f'A{row}'] = "📈 Quartalsergebnisse"
    ws[f'A{row}'].font = Font(bold=True, size=14, color="667eea")

    row += 2
    headers = ['Quartal', 'Verkaufspreis', 'Absatz', 'Umsatz', 'Kosten', 'Nettogewinn', 'Kasse', 'Lager']
    for col, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = border

    row += 1
    for result in simulator.results:
        ws.cell(row=row, column=1, value=f"Q{result.quarter}")
        ws.cell(row=row, column=2, value=f"{result.sales_price:.2f} M")
        ws.cell(row=row, column=3, value=f"{result.sales_volume} Lose")
        ws.cell(row=row, column=4, value=f"{result.sales_revenue:.2f} M")
        ws.cell(row=row, column=5, value=f"{result.total_cost:.2f} M")
        ws.cell(row=row, column=6, value=f"{result.net_profit:.2f} M")
        ws.cell(row=row, column=7, value=f"{result.cash_ending:.2f} M")
        ws.cell(row=row, column=8, value=f"{result.finished_goods_inventory} Lose")

        # Color code profit
        if result.net_profit >= 0:
            ws.cell(row=row, column=6).fill = positive_fill
            ws.cell(row=row, column=6).font = Font(color="22543d")
        else:
            ws.cell(row=row, column=6).fill = negative_fill
            ws.cell(row=row, column=6).font = Font(color="742a2a")

        # Apply borders
        for col in range(1, 9):
            ws.cell(row=row, column=col).border = border
            ws.cell(row=row, column=col).alignment = Alignment(horizontal='center')

        row += 1

    # Detailed cost breakdown
    row += 2
    ws.merge_cells(f'A{row}:H{row}')
    ws[f'A{row}'] = "💰 Detaillierte Kostenaufstellung"
    ws[f'A{row}'].font = Font(bold=True, size=14, color="667eea")

    row += 2
    cost_headers = ['Quartal', 'Material', 'Fertigung', 'Montage', 'Gemeinkosten', 'Marketing', 'Gesamt']
    for col, header in enumerate(cost_headers, start=1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = border

    row += 1
    for result in simulator.results:
        ws.cell(row=row, column=1, value=f"Q{result.quarter}")
        ws.cell(row=row, column=2, value=f"{result.material_cost:.2f} M")
        ws.cell(row=row, column=3, value=f"{result.production_cost:.2f} M")
        ws.cell(row=row, column=4, value=f"{result.assembly_cost:.2f} M")
        ws.cell(row=row, column=5, value=f"{result.overhead_cost:.2f} M")
        ws.cell(row=row, column=6, value=f"{result.marketing_cost:.2f} M")
        ws.cell(row=row, column=7, value=f"{result.total_cost:.2f} M")

        for col in range(1, 8):
            ws.cell(row=row, column=col).border = border
            ws.cell(row=row, column=col).alignment = Alignment(horizontal='center')

        row += 1

    # Adjust column widths
    ws.column_dimensions['A'].width = 12
    ws.column_dimensions['B'].width = 18
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 15
    ws.column_dimensions['H'].width = 15

    # Add row height for title
    ws.row_dimensions[1].height = 25

    # Create exports directory if it doesn't exist
    exports_dir = os.path.join(os.getcwd(), 'exports')
    os.makedirs(exports_dir, exist_ok=True)

    # Save file
    filename = f"Factory_Ergebnisse_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    filepath = os.path.join(exports_dir, filename)
    wb.save(filepath)

    return send_file(filepath, as_attachment=True, download_name=filename)


if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    os.makedirs('exports', exist_ok=True)

    # Use environment variable for port (for cloud deployment)
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV') != 'production'

    app.run(debug=debug, host='0.0.0.0', port=port)
