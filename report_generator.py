import matplotlib.pyplot as plt

def format_currency(value):
    """
    Formatea un número como moneda con separadores de miles y símbolo de dólar.
    """
    return f"${value:,.2f}"  # Formato: $1,234.56

def generate_consolidated_report(analysis):
    """
    Genera un reporte consolidado basado en el análisis por empresa.
    """
    report = "Análisis Consolidado de Ventas:\n"
    report += "-----------------------------------\n"

    for company, stats in analysis.items():
        report += f"Sede: {company}\n"
        report += f"  Total Ventas Reales: {format_currency(stats['total'])}\n"
        report += f"  Promedio Ventas Reales: {format_currency(stats['average'])}\n"
        report += f"  Venta Máxima: {format_currency(stats['max'])}\n"
        report += f"  Venta Mínima: {format_currency(stats['min'])}\n"
        report += f"  Margen de Ganancia Promedio: {format_currency(stats['profit_margin'])}\n"
        report += "-----------------------------------\n"

    return report

def generate_chart(data, output_file):
    """
    Genera un gráfico de barras de ventas reales agrupadas por sede y lo guarda localmente.
    """
    grouped = data.groupby('Sede')['Precio Venta Real'].sum()
    grouped.plot(kind='bar', title='Ventas Reales por Empresa')
    plt.ylabel('Total Ventas Reales ($)')
    plt.xlabel('Sedes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

