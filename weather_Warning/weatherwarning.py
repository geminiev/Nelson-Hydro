import urllib.request, json

WEATHER_API_KEY = 'ec8cd7ffbb7640119e5210453220905'
LOCATION = '49.4928, -117.2948'
URL = "https://api.weatherapi.com/v1/forecast.json?key=${WEATHER_API_KEY}&q=${LOCATION}&aqi=no"
WIND_THRESHOLD = 40
GUST_THRESHOLD = 60
count = 0

def weatherWarning():
    with urllib.request.urlopen(URL)
    data = json.loads(url.read().decode())

    wind_kph = ['data']['forecast']['wind_kph']
    gust_kph = ['data']['forecast']['gust_kph']

    if wind_kph > WIND_THRESHOLD:
        #email a warning
    if gust_kph > GUST_THRESHOLD:
        #email a warning
    

    return