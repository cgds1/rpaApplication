from twilio.rest import Client

# Configuración de Twilio (configurar segunn los datos de la pagina)
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def send_report_via_whatsapp(report, to_number, image_path=None):
    """
    Envía un reporte de texto y opcionalmente una imagen a través de WhatsApp utilizando Twilio.

    Args:
        report (str): El texto del reporte.
        to_number (str): El número de WhatsApp del destinatario en formato internacional.
        image_path (str, optional): URL de la imagen a enviar.
    """
    try:
        if image_path:
            # Enviar mensaje con texto e imagen (URL de la nube)
            message = client.messages.create(
                from_='whatsapp:+1',  # Número de Twilio (sandbox)
                body=report,
                to=f'whatsapp:{to_number}',
                media_url=[image_path]
            )
        print("Mensaje enviado con éxito, SID:", message.sid)
    except Exception as e:
        print("Error al enviar el mensaje:", e)
