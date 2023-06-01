'''Create a command-line tool that accepts a city's name and returns the current weather forecast.
Leverage OpenWeatherMap API to fetch weather data and parse it using Python.'''
import requests
import config
def main():
    # TODO_HL: Get API key from https://openweathermap.org/appid
    # TODO_HL: Get city name from command line
    city_name = input("Enter city name : ")
    # TODO_HL: HIDE API KEY
    api_key= config.api_key

    # TODO_HL: Get current weather data for the city
    # TODO_HL: Display weather data in a readable format

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        print("Weather Data for " + city_name + ":")
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print(" Temperature (in kelvin unit) = " + str(current_temperature) + "\n Atmospheric pressure (in hPa unit) = " + str(current_pressure) + "\n Humidity (in percentage) = " + str(current_humidity) + "\n Description = " + str(weather_description))
    else:
        print(" City Not Found ")
if __name__ == "__main__":
    main()