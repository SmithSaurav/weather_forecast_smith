import requests
from datetime import datetime


def getLocation():
    try:
        r = requests.get(f'http://ip-api.com/json').json()
        return {
            'city': r['city'],
            'regionName': r['region'],
            'country': r['country'],
            'timezone': r['timezone'],
            'loc': f"lon={r['lon']},lat={r['lat']}"
        }
    except Exception as e:
        print(e)


def image_url(day_desc, is_night):
    if is_night:
        if "snow" in day_desc.lower():
            return "/images/night_snow.gif"
        elif "cloud" in day_desc.lower():
            return "/images/night_colunds.gif"
        elif "fog" in day_desc.lower():
            return "/images/night_fog.gif"
        elif "rain" in day_desc.lower():
            return "/images/night_rain.gif"
        elif "clear" in day_desc.lower():
            return "/images/night_clear.gif"
        elif "thunderstorm" in day_desc.lower():
            return "/images/night_thunderstorm.gif"
        else:
            return "/images/night_clear.gif"
    else:
        if "snow" in day_desc.lower():
            return "https://mdbgo.io/ascensus/mdb-advanced/img/snow.gif"
        elif "cloud" in day_desc.lower():
            return "https://mdbgo.io/ascensus/mdb-advanced/img/clouds.gif"
        elif "fog" in day_desc.lower():
            return "https://mdbgo.io/ascensus/mdb-advanced/img/fog.gif"
        elif "rain" in day_desc.lower():
            return "https://mdbgo.io/ascensus/mdb-advanced/img/rain.gif"
        elif "clear" in day_desc.lower():
            return "https://mdbgo.io/ascensus/mdb-advanced/img/clear.gif"
        elif "thunderstorm" in day_desc.lower():
            return "https://mdbgo.io/ascensus/mdb-advanced/img/thunderstorm.gif"
        else:
            return "https://mdbgo.io/ascensus/mdb-advanced/img/clear.gif"


def get_weather(weatherstack_api_key, location, units='m', current=None):
    try:
        # Create the API url with the location and units parameters
        url = f"http://api.weatherstack.com/forecast?access_key={weatherstack_api_key}&query={location}&units={units}"
        # Send a GET request to the API url
        response = requests.get(url)

        if response.status_code == 200:
            # If the response status code is 200, then retrieve the JSON data from the response
            data = response.json()
            if current:
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime("%H:%M - %A, %d %b '%y")
                current_hour = current_datetime.hour
            else:
                localtime = data['location']['localtime']
                current_hour = int(localtime.split()[1].split(':')[0])
                localtime = datetime.strptime(localtime, '%Y-%m-%d %H:%M')
                formatted_datetime = localtime.strftime("%H:%M - %A, %d %b '%y")
            night_start_hour = 18  # 6 PM
            night_end_hour = 6  # 6 AM
            is_night = night_start_hour <= current_hour <= 23 or 0 <= current_hour <= night_end_hour
            # Extract the required weather data from the JSON object and store it in a dictionary
            weather = {
                "pressure": data["current"]["pressure"],
                "location": data["location"]["name"],
                "temperature": data["current"]["temperature"],
                "humidity": data["current"]["humidity"],
                "wind_speed": data["current"]["wind_speed"],
                "description": data["current"]["weather_descriptions"][0],
                "icon": data["current"]["weather_icons"][0],
                "forecast": data.get("forecast", {}).get("forecastday", [{}])[0].get("day", {}).get("condition",
                                                                                                    {}).get("text", ""),
                "forecast_icon": data.get("forecast", {}).get("forecastday", [{}])[0].get("day", {}).get("condition",
                                                                                                         {}).get("icon",
                                                                                                                 {}).get(
                    "url", ""),
                "current_datetime": formatted_datetime,
                "img_url": image_url(data["current"]["weather_descriptions"][0], is_night)

            }
            return 200, weather
        else:
            return response.status_code, {'error': "Could not retrieve weather data."}
    except Exception as e:
        print(e)
        return 500, {'error': e}
