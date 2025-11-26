"""
Flask Web Application for Factory Business Simulation
Provides web-based interface for the game
Includes Abschreibungen, Zinsen, and Steuern
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
        },
        'financial_params': {
            'depreciation_per_quarter': params.depreciation_per_quarter,
            'interest_per_quarter': params.interest_per_quarter,
            'tax_rate': params.tax_rate * 100
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
        'herstellungskosten': result.herstellungskosten,
        'overhead_cost': result.overhead_cost,
        'marketing_cost': result.marketing_cost,
        'depreciation': result.depreciation,
        'interest': result.interest,
        'total_operating_cost': result.total_operating_cost,
        'gross_profit': result.gross_profit,
        'ebit': result.ebit,
        'profit_before_tax': result.profit_before_tax,
        'tax': result.tax,
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
                'herstellungskosten': r.herstellungskosten,
                'gross_profit': r.gross_profit,
                'ebit': r.ebit,
                'profit_before_tax': r.profit_before_tax,
                'tax': r.tax,
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
    """Export game results as Excel file with full GuV structure"""
    game_id = request.args.get('game_id', 'default')

    if game_id not in simulators:
        return jsonify({'success': False, 'error': 'Game not found'}), 404

    simulator = simulators[game_id]
    summary = simulator.get_summary()

    # Create workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "GuV und Jahresabschluss"

    # Styling
    header_fill = PatternFill(start_color="667eea", end_color="667eea", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=12)
    title_font = Font(bold=True, size=16, color="2d3748")
    subtitle_font = Font(size=11, color="718096")

    positive_fill = PatternFill(start_color="c6f6d5", end_color="c6f6d5", fill_type="solid")
    negative_fill = PatternFill(start_color="fed7d7", end_color="fed7d7", fill_type="solid")
    highlight_fill = PatternFill(start_color="e6f3ff", end_color="e6f3ff", fill_type="solid")

    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    # Title section
    ws.merge_cells('A1:J1')
    ws['A1'] = "🏭 Factory Business Simulation - Gewinn- und Verlustrechnung"
    ws['A1'].font = title_font
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')

    ws.merge_cells('A2:J2')
    ws['A2'] = "Planspiel BWL für BDE - WiSe 2025/26"
    ws['A2'].font = subtitle_font
    ws['A2'].alignment = Alignment(horizontal='center')

    ws.merge_cells('A3:J3')
    ws['A3'] = "Ostfalia Hochschule für angewandte Wissenschaften"
    ws['A3'].font = subtitle_font
    ws['A3'].alignment = Alignment(horizontal='center')

    ws.merge_cells('A4:J4')
    ws['A4'] = f"Erstellt am: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
    ws['A4'].font = subtitle_font
    ws['A4'].alignment = Alignment(horizontal='center')

    # GuV section - like in original Factory document
    row = 6
    ws.merge_cells(f'A{row}:J{row}')
    ws[f'A{row}'] = "📊 GEWINN- UND VERLUSTRECHNUNG (GuV)"
    ws[f'A{row}'].font = Font(bold=True, size=14, color="667eea")

    row += 2
    guv_headers = ['Position', 'Q1', 'Q2', 'Q3', 'Q4', 'GESAMT']
    for col, header in enumerate(guv_headers, start=1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = border

    row += 1
    
    # Umsatzerlöse
    ws.cell(row=row, column=1, value="Umsatzerlöse").font = Font(bold=True)
    for i, result in enumerate(simulator.results, start=2):
        ws.cell(row=row, column=i, value=result.sales_revenue).number_format = '0.00" M"'
        ws.cell(row=row, column=i).border = border
        ws.cell(row=row, column=i).fill = positive_fill
    ws.cell(row=row, column=6, value=summary['total_revenue']).number_format = '0.00" M"'
    ws.cell(row=row, column=6).font = Font(bold=True)
    ws.cell(row=row, column=6).border = border
    ws.cell(row=row, column=6).fill = positive_fill
    row += 1
    
    # Herstellungskosten
    ws.cell(row=row, column=1, value="Herstellungskosten").font = Font(bold=True)
    for i, result in enumerate(simulator.results, start=2):
        ws.cell(row=row, column=i, value=result.herstellungskosten).number_format = '0.00" M"'
        ws.cell(row=row, column=i).border = border
        ws.cell(row=row, column=i).fill = negative_fill
    ws.cell(row=row, column=6, value=summary['total_herstellungskosten']).number_format = '0.00" M"'
    ws.cell(row=row, column=6).font = Font(bold=True)
    ws.cell(row=row, column=6).border = border
    ws.cell(row=row, column=6).fill = negative_fill
    row += 1
    
    # Bruttoergebnis
    ws.cell(row=row, column=1, value="= Bruttoergebnis").font = Font(bold=True, italic=True)
    for i, result in enumerate(simulator.results, start=2):
        ws.cell(row=row, column=i, value=result.gross_profit).number_format = '0.00" M"'
        ws.cell(row=row, column=i).border = border
        ws.cell(row=row, column=i).fill = highlight_fill
        ws.cell(row=row, column=i).font = Font(bold=True)
    ws.cell(row=row, column=6, value=summary['total_gross_profit']).number_format = '0.00" M"'
    ws.cell(row=row, column=6).font = Font(bold=True, size=12)
    ws.cell(row=row, column=6).border = border
    ws.cell(row=row, column=6).fill = highlight_fill
    row += 1
    
    # Gemeinkosten
    ws.cell(row=row, column=1, value="Gemeinkosten")
    for i, result in enumerate(simulator.results, start=2):
        ws.cell(row=row, column=i, value=result.overhead_cost + result.marketing_cost).number_format = '0.00" M"'
        ws.cell(row=row, column=i).border = border
    ws.cell(row=row, column=6, value=summary['total_overhead'] + summary['total_marketing']).number_format = '0.00" M"'
    ws.cell(row=row, column=6).border = border
    row += 1
    
    # Abschreibungen
    ws.cell(row=row, column=1, value="Abschreibungen").font = Font(bold=True, color="d97706")
    for i, result in enumerate(simulator.results, start=2):
        ws.cell(row=row, column=i, value=result.depreciation).number_format = '0.00" M"'
        ws.cell(row=row, column=i).border = border
        ws.cell(row=row, column=i).font = Font(color="d97706")
    ws.cell(row=row, column=6, value=summary['total_depreciation']).number_format = '0.00" M"'
    ws.cell(row=row, column=6).font = Font(bold=True, color="d97706")
    ws.cell(row=row, column=6).border = border
    row += 1
    
    # Betriebsergebnis (EBIT)
    ws.cell(row=row, column=1, value="= Betriebsergebnis (EBIT)").font = Font(bold=True, italic=True)
    for i, result in enumerate(simulator.results, start=2):
        ws.cell(row=row, column=i, value=result.ebit).number_format = '0.00" M"'
        ws.cell(row=row, column=i).border = border
        ws.cell(row=row, column=i).fill = highlight_fill
        ws.cell(row=row, column=i).font = Font(bold=True)
    ws.cell(row=row, column=6, value=summary['total_ebit']).number_format = '0.00" M"'
    ws.cell(row=row, column=6).font = Font(bold=True, size=12)
    ws.cell(row=row, column=6).border = border
    ws.cell(row=row, column=6).fill = highlight_fill
    row += 1
    
    # Zinsen
    ws.cell(row=row, column=1, value="Zinsen").font = Font(bold=True, color="dc2626")
    for i, result in enumerate(simulator.results, start=2):
        ws.cell(row=row, column=i, value=result.interest).number_format = '0.00" M"'
        ws.cell(row=row, column=i).border = border
        ws.cell(row=row, column=i).font = Font(color="dc2626")
    ws.cell(row=row, column=6, value=summary['total_interest']).number_format = '0.00" M"'
    ws.cell(row=row, column=6).font = Font(bold=True, color="dc2626")
    ws.cell(row=row, column=6).border = border
    row += 1
    
    # Gewinn vor Steuern
    ws.cell(row=row, column=1, value="= Gewinn vor Steuern").font = Font(bold=True, italic=True)
    for i, result in enumerate(simulator.results, start=2):
        ws.cell(row=row, column=i, value=result.profit_before_tax).number_format = '0.00" M"'
        ws.cell(row=row, column=i).border = border
        ws.cell(row=row, column=i).fill = highlight_fill
        ws.cell(row=row, column=i).font = Font(bold=True)
    ws.cell(row=row, column=6, value=summary['total_profit_before_tax']).number_format = '0.00" M"'
    ws.cell(row=row, column=6).font = Font(bold=True, size=12)
    ws.cell(row=row, column=6).border = border
    ws.cell(row=row, column=6).fill = highlight_fill
    row += 1
    
    # Steuern
    ws.cell(row=row, column=1, value="Steuern (33,33%)").font = Font(bold=True, color="dc2626")
    for i, result in enumerate(simulator.results, start=2):
        ws.cell(row=row, column=i, value=result.tax).number_format = '0.00" M"'
        ws.cell(row=row, column=i).border = border
        ws.cell(row=row, column=i).font = Font(color="dc2626")
    ws.cell(row=row, column=6, value=summary['total_tax']).number_format = '0.00" M"'
    ws.cell(row=row, column=6).font = Font(bold=True, color="dc2626")
    ws.cell(row=row, column=6).border = border
    row += 1
    
    # Gewinn nach Steuern
    ws.cell(row=row, column=1, value="= GEWINN NACH STEUERN").font = Font(bold=True, size=12, color="22543d")
    for i, result in enumerate(simulator.results, start=2):
        cell = ws.cell(row=row, column=i, value=result.net_profit)
        cell.number_format = '0.00" M"'
        cell.border = border
        if result.net_profit >= 0:
            cell.fill = positive_fill
            cell.font = Font(bold=True, color="22543d")
        else:
            cell.fill = negative_fill
            cell.font = Font(bold=True, color="742a2a")
    cell = ws.cell(row=row, column=6, value=summary['total_net_profit'])
    cell.number_format = '0.00" M"'
    cell.border = border
    if summary['total_net_profit'] >= 0:
        cell.fill = positive_fill
        cell.font = Font(bold=True, size=13, color="22543d")
    else:
        cell.fill = negative_fill
        cell.font = Font(bold=True, size=13, color="742a2a")

    # Summary section
    row += 3
    ws.merge_cells(f'A{row}:J{row}')
    ws[f'A{row}'] = "📈 JAHRESABSCHLUSS - WICHTIGE KENNZAHLEN"
    ws[f'A{row}'].font = Font(bold=True, size=14, color="667eea")

    row += 2
    summary_data = [
        ['Gesamte Abschreibungen (Jahr)', f"{summary['total_depreciation']:.2f} M", 'info'],
        ['Gesamte Zinsen (Jahr)', f"{summary['total_interest']:.2f} M", 'info'],
        ['Gesamte Steuern (Jahr)', f"{summary['total_tax']:.2f} M", 'info'],
        ['', '', ''],
        ['Durchschn. Gewinn pro Quartal', f"{summary['average_profit_per_quarter']:.2f} M", ''],
        ['Umsatzrendite', f"{summary['return_on_sales']:.2f}%", ''],
        ['Endbestand Kasse', f"{summary['final_cash']:.2f} M", 'positive'],
    ]

    for label, value, style in summary_data:
        if label:
            ws[f'B{row}'] = label
            ws[f'B{row}'].font = Font(bold=True)
            ws[f'D{row}'] = value
            ws[f'D{row}'].font = Font(bold=True, size=12)

            if style == 'positive':
                ws[f'D{row}'].fill = positive_fill
                ws[f'D{row}'].font = Font(bold=True, size=12, color="22543d")
            elif style == 'info':
                ws[f'D{row}'].font = Font(bold=True, size=12, color="d97706")

        row += 1

    # Adjust column widths
    ws.column_dimensions['A'].width = 30
    for col in ['B', 'C', 'D', 'E', 'F']:
        ws.column_dimensions[col].width = 15

    # Add row height for title
    ws.row_dimensions[1].height = 25

    # Create exports directory if it doesn't exist
    exports_dir = os.path.join(os.getcwd(), 'exports')
    os.makedirs(exports_dir, exist_ok=True)

    # Save file
    filename = f"Factory_GuV_Jahresabschluss_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
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
