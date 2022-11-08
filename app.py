import requests
import smtplib

headers = {'Accept': 'application/json'}

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('dossierbootcamp57@gmail.com', 'izorvmsqxlzridtt')

response = requests.get('https://api.coincap.io/v2/assets/bitcoin', headers=headers)

timestamp = response.json()['timestamp']
price = response.json()['data']['priceUsd']

server.sendmail('dossierbootcamp57@gmail.com', 'mohd.abazeemabazeem@gmail.com', f'Todays bitcoin price is as on {timestamp} is {price}')

print('Mail sent successfully')