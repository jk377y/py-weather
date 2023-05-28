# used to GET weather information from the OpenWeatherMap API
import requests
# used to convert the JSON response to a Python dictionary (object)
import json

# converts Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin_temp):
    return round((kelvin_temp - 273.15) * 9/5 + 32, 2)

# converts meters per second to miles per hour
def mps_to_mph(mps_speed):
    return round(mps_speed * 2.237, 2)

# main function
def weather():
    print("=== Weather Application ===")
    # get the city from the user
    city = input("Enter the name of a city: ")

    # my API key, replace with your own (they are FREE!)
    api_key = "d01afd2806e508d282da4f840dd4696a"
    # base URL for the OpenWeatherMap API (used for fetching weather data)
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # make a GET request to the OpenWeatherMap API
    response = requests.get(base_url)
    # convert the JSON response to a Python dictionary (object) and store it in a variable called data
    data = json.loads(response.text)

    # check if the city was found; data.cod value will be 200 if found. 404 if not found. (see image on README.md for example)
    if data["cod"] == "404":
        print(f"Weather information not found for '{city}'. Please try again.")
    
    # if the city was found, assign the weather information from the data dictionary (key-value pairs) to variables
    else:
        main_weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temperature = kelvin_to_fahrenheit(data["main"]["temp"])
        humidity = data["main"]["humidity"]
        wind_speed = mps_to_mph(data["wind"]["speed"])

        # print the weather information to the user (see image on README.md for example)
        print(f"Weather Information for '{city}':")
        print(f"Main Weather: {main_weather}")
        print(f"Description: {description}")
        print(f"Temperature: {temperature} °F")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} mph")

# the weather function is called when the file is run
weather()