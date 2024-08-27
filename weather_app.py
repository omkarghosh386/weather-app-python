import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data.get("main", {})
        temperature = main.get("temp", "N/A")
        humidity = main.get("humidity", "N/A")
        pressure = main.get("pressure", "N/A")
        weather_description = data["weather"][0].get("description", "N/A")
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "7f7ba1f8b2a5159964ab91cf487cbc93"  # Replace with your OpenWeatherMap API key
    get_weather(city_name, api_key)