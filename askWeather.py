# This is a python3 script that does an HTTP GET to openweather.com, asking
# for weather forecast near the city you want

import http.client
import json

connection = http.client.HTTPConnection("api.openweathermap.org")

city = input("Inserisci la tua citta: ")
resource = "/data/2.5/weather?q=%s&appid=03ad22cf53590930baf9b706a892c49c"%city
connection.request("GET", resource)
response = connection.getresponse()
body = response.read().decode()

# Da object_python a JSON
# json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

# Da JSON a object_python
# json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

data_json = json.loads(body)
print(data_json)

