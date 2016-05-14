from django import template
import json
import requests

register = template.Library()

@register.filter
def bitcoin(value):

    url = 'http://bitcoinkopen.com/api/daycourses.json'
    request = requests.get(url)
    data = json.loads(request.text)[0]
    get_rate_of_exchange = data['EUR']['24h']

    btc = ((value / 100.0) / float(get_rate_of_exchange))
    t = 10.0**6
    return round(btc * t / t, 6)
