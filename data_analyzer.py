def analyze_data_by_company(data):
    """
    Realiza el análisis financiero y estadístico de los datos agrupados por Sede.
    """
    grouped = data.groupby('Sede')
    analysis = {}

    for company, group in grouped:
        total_ventas = group['Precio Venta Real'].sum()
        promedio_ventas = group['Precio Venta Real'].mean()
        venta_max = group['Precio Venta Real'].max()
        venta_min = group['Precio Venta Real'].min()
        margen_ganancia = (group['Precio Venta Real'] - group['Costo Vehículo']).mean()

        analysis[company] = {
            'total': total_ventas,
            'average': promedio_ventas,
            'max': venta_max,
            'min': venta_min,
            'profit_margin': margen_ganancia
        }

    return analysis
