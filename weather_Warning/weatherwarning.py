# Script to warn the PIC that inclement wind is coming.
# Scrapes weatherapi.com to find data on forecasted wind conditions coming to Nelson.
# Goal: Allow PIC to put more people on shift if weather is looking scary.
# Sends email from nhydroautomation@gmail.com.
# Author: Eve Sankar | esankar@nelson.ca | May 25th, 2022\
# DOESNT WORK BECAUSE GOOGLE ASSUMES ITS USERS ARE IDIOTS :))))))))))))))))))))))

import urllib.request, json, time

WEATHER_API_KEY = 'ec8cd7ffbb7640119e5210453220905'
LOCATION = '49.4928, -117.2948'
WEBSITE = "https://api.weatherapi.com/v1/forecast.json?key=${WEATHER_API_KEY}&q=${LOCATION}&aqi=no"
WIND_THRESHOLD = 0 # make 40 normally, 0 for testing
GUST_THRESHOLD = 0 # 0 for testing
count = 0

def main():
    while True:
        weatherWarning()
        time.sleep(24.0 * 60.0 * 60.0) # 24 hours in seconds
    return

def weatherWarning():
    with urllib.request.urlopen(WEBSITE) as url:
        data = json.loads(url.read().decode())

    wind_kph = ['data']['forecast']['wind_kph']
    gust_kph = ['data']['forecast']['gust_kph']

    if wind_kph > WIND_THRESHOLD:
        #email a warning
    if gust_kph > GUST_THRESHOLD:
        #email a warning

    return