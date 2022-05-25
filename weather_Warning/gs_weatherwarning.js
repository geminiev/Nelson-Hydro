// Script to warn the PIC that inclement wind is coming.
// Scrapes weatherapi.com to find data on forecasted wind conditions coming to Nelson.
// Goal: Allow PIC to put more people on shift if weather is looking scary.
// Sends email from nhydroautomation@gmail.com.
// Author: Eve Sankar | esankar@nelson.ca | May 25th, 2022

function fetchForecast()
{  
  // Fetch WeatherAPI query
  const apiKey = 'ec8cd7ffbb7640119e5210453220905'
  const coordinates = '49.4928, -117.2948'
  const weatherUrl = "https://api.weatherapi.com/v1/forecast.json?key=ec8cd7ffbb7640119e5210453220905&q=49.4928,%20-117.2948&aqi=no"
  const gust_threshold = 30; // suggested 30kmh
  const wind_threshold = 30; // suggested 30kmh

  var response = UrlFetchApp.fetch(weatherUrl);

  // Parse the JSON reply
  var json = response.getContentText();
  var data = JSON.parse(json);

  // Get a few of the weather variables
  var temp = data.forecast.forecastday[0].day.maxtemp_c
  var gust, wind, wind_time, gust_time;
  var maxwind = 0;
  var maxgust = 0;

  // Cycle through each hour of the day
  for (var count = 0; count < 24; count++) {
    gust = data.forecast.forecastday[0].hour[count].gust_kph
    wind = data.forecast.forecastday[0].hour[count].wind_kph
    wind_degree = data.forecast.forecastday[0].hour[count].wind_degree
    wind_dir = data.forecast.forecastday[0].hour[count].wind_dir
    day = data.forecast.forecastday[0].date

    if (maxgust < gust) {
      maxgust = gust;
      gust_time = count;
    }
    
    if (maxwind < wind) {
      maxwind = wind;
      wind_time = count;
    }
  }

  // Check if speeds exceed threshold
  if ((maxgust > gust_threshold) && (maxwind > wind_threshold)) {
      MailApp.sendEmail({
      to: 'jprocyshyn@nelson.ca',
      subject: 'Gust and Wind Warning ' + day,
      htmlBody: 'Hello. Our weather scraping has detected an incoming gust of ' + maxgust + ' kmh and an incoming wind of ' + maxwind + ' kmh from ' + wind_degree + ' degrees ' + wind_dir + '.' + ' This has the potential to damage critical NH infrastructure. These will peak at ' + gust_time + ':00 ' + 'and ' + wind_time + ':00' + ' military time respectively.'
  });
    }
  else if (maxgust > gust_threshold) {
      MailApp.sendEmail({
      to: 'jprocyshyn@nelson.ca',
      subject: 'Gust Warning ' + day,
      htmlBody: 'Hello. Our weather system has detected an incoming gust of ' + maxgust + ' kmh' + ' from ' + wind_degree + ' degrees ' + wind_dir + '.' + ' This will peak at ' + gust_time + ':00' + ' military time.'
  });
    }
  else if (maxwind > wind_threshold) {
      MailApp.sendEmail({
      to: 'jprocyshyn@nelson.ca',
      subject: 'Wind Warning ' + day,
      htmlBody: 'Hello. Our weather system has detected an incoming wind of ' + maxwind + ' kmh' + ' from ' + wind_degree + ' degrees ' + wind_dir + '.' + 'This will peak at ' + wind_time + ':00' + ' military time.'
  });
    }

}