from django import template
import json
import requests

register = template.Library()

@register.filter
def bitcoin(value, exchange_rate=None):
    if exchange_rate is None:
        url = 'http://bitcoinkopen.com/api/daycourses.json'
        request = requests.get(url)
        data = json.loads(request.text)[0]
        exchange_rate = data['EUR']['24h']

    btc = ((value / 100.0) / float(exchange_rate))
    t = 10.0**6
    return round(btc * t / t, 6)
