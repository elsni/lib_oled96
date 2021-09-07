#!/usr/bin/env python
# coding=utf-8

# ---------------------------------------------------------------------------------
# Lade Aktuelle Wetterdaten vom openweathermap und zeige sie
# auf einem joyit 0.96" OLED Display an, welches über 12c angesteuert wird.
# https://joy-it.net/en/products/SBC-OLED01

# Bibliotheken importieren
import requests
import json
from lib_oled96 import ssd1306
from smbus import SMBus
from time import sleep
from PIL import ImageFont


# die Openwethermap APP-ID
APPID='<your APP ID>'

# Display einrichten
i2cbus = SMBus(1)            # 0 = Raspberry Pi 1,Odroid C4, 1 = Raspberry Pi 2,3,4,zero
oled = ssd1306(i2cbus)

# Ein paar Abkürzungen, um den Code zu entschlacken
draw = oled.canvas


r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=L%C3%BCbeck&appid={APPID}&units=metric')
j = json.loads(r.text)
outtemp = j['main']['temp']
outpr= j['main']['pressure']
outhum=j['main']['humidity']

# Display zum Start löschen
oled.cls()
oled.display()

font = ImageFont.truetype('FreeSans.ttf', 34)
draw.text((0, 0), f'{outtemp:.1f}°C', font=font, fill=1)
font = ImageFont.truetype('FreeSans.ttf', 14)
draw.text((0, 34), f'{outhum:.1f}%', font=font, fill=1)
draw.text((0, 48), f'{outpr} hpa', font=font, fill=1)

# Ausgaben auf Display schreiben
oled.display()
sleep(10)
oled.cls()
oled.onoff(0)

