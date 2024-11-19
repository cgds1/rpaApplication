from data_analyzer import analyze_data_by_company
from report_generator import generate_consolidated_report, generate_chart
from whatsapp_sender import send_report_via_whatsapp
import pandas as pd

# Ruta del archivo Excel
EXCEL_FILE = "ventas.xlsx"

def main():
    # Leer datos del archivo Excel (hoja VENTAS)
    data = pd.read_excel(EXCEL_FILE, sheet_name='VENTAS')

    # Análisis agrupado por empresa (Sede)
    analysis = analyze_data_by_company(data)

    # Generar reporte consolidado y gráfico
    report = generate_consolidated_report(analysis)
    chart_url = "https://raw.githubusercontent.com/cgds1/rpaApplication/main/ventas_grafico.png"  # URL de la imagen en la nube 
    # generate_chart(data, "ventas_grafico.png");  (Crea el gráfico local)

    # Enviar reporte por WhatsApp
    to_whatsapp_number = ""  # Cambia este número por el verificado en Twilio
    send_report_via_whatsapp(report, to_whatsapp_number, image_path=chart_url)

if __name__ == "__main__":
    main()
