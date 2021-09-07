# Script um einen Wetter.datensatz an Datacake zu senden.
# Die wetterdaten werden von www.openweathermap.org geladen
# aktuell in S3Test/TestDevice
# Das in Datacace angelegte Gerät hat drei Datenfelder: temperature, moisture, pressure

import requests
import json

# API Key
DTCK_KEY = 'b7a05d36589a872f93ea4ba52d5b7c9bf132fbaf'

# Device Seriennummer
# Die Device-Id ist NICHT die offensichtliche Device id, sondern die Id die man unter
# /Device/Configure/Integrations/MQTT/Configure als Bestandteil des Topics erfährt.
DTCK_DEVICE_ID= '81f53bcc-aa44-4c22-b7c1-eb1027434ab4'

# Produkt URL. Wenn an diese URL gesendet wird, kann ein optionaler Payload Decoder konfigurierrt werden
URL_PRODUCT='https://iot-safetysolutions-draeger.com/api/integrations/api/ebd127a2-e579-4c8b-8b55-86f8e3922f46/'

# API URL. mit dieser URL lassen sich Datensätze ohne Decoder senden sofern sie im u.a. JSON-Format sind
URL_API=f'https://api.datacake.co/v1/devices/{DTCK_DEVICE_ID}/record/?batch=true'

# die Openwethermap APP-ID
APPID='b702c266e5dfbee0472987f9c8651d11'


if __name__ == "__main__":

    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=L%C3%BCbeck&appid={APPID}&units=metric')
    j = json.loads(r.text)
    outtemp = j['main']['temp']
    outpr= j['main']['pressure']
    outhum=j['main']['humidity']

    requests.post(URL_API, headers={"Authorization": f"Token {DTCK_KEY}"}, json=[
        {
            "field": "TEMPERATURE",
            "value": outtemp
        },
        {
            "field": "MOISTURE",
            "value": outhum
        },
        {
            "field": "PRESSURE",
            "value": outpr
        }
    ])


