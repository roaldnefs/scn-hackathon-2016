#!/usr/bin/env python3
import requests

from flask import Flask
from flask import request

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Maak een Flash app.
app = Flask(__name__)

# Maak een wallet object.
wallet = Wallet()

# Maak een payment app, gecombineerd met de app en wallet objecten.
payment = Payment(app, wallet)


# Functie om een input naar int om te zetten.
def to_int(input):
    # Is er een dag args mee gegeven?
    if input is not None:
        # Ja, dus sla op als int.
        days = int(input)
    else:
        # Nee, dus maak van days 1.
        days = 1

    # Gaat het om een int?
    if not isinstance(days, int):
        # Nee, dus maak days = 1
        days = 1

    return days


# Functie om de prijs te berekenen.
def calc_price(request):
    # Haal het aantal dagen als int op.
    days = to_int(request.args.get('days'))

    # Return het bedrag.
    return (days * 1000)


# Onderstaande functie wordt uitgevoerd wanneer /pay aangeroepen wordt.
# Een prijs wordt verplicht, die door de functie calc_price() wordt berekend.
@app.route('/pay')
@payment.required(calc_price)
def pay():
    # Maak een request aan naar de Django server.
    r = requests.get('http://***REMOVED***:8000/pay/' + request.args.get('reference') + '/' + str(to_int(request.args.get('days'))))

    # Is de request gelukt?
    if (r.status_code == 200):
        # Geef dan 'OK' terug naar de client.
        return 'OK'
    else:
        # Request mislukt, geef 'FAIL' terug.
        return 'FAIL'


# Initialize de server.
if __name__ == '__main__':
    app.run(host='***REMOVED***')
