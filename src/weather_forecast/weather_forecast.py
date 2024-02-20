import requests
from pathlib import Path
import json


def get_weather_forecast(latitude: float, longitude: float, api_key: str):
    """
    Makes a GET request to openweathermap's API.
    Documentation for used API: https://openweathermap.org/forecast5
    :param latitude: Latitude coordinate for the desired location
    :param longitude: Longitude coordinate for the desired location
    :param api_key: Openweathermap API KEY
    :return: ---
    """

    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                            params={"lat": latitude, "lon": longitude, "appid": api_key})

    return response.json()


if __name__ == '__main__':
    project_root = Path(__file__).parents[2]

    # Get api key
    with open(project_root / "credentials.json", 'r') as f:
        data = json.load(f)
        api_key_val = data["openweather"]["key"]

    # Get location coords
    with open(project_root / "config.json", 'r') as f:
        data = json.load(f)
        latitude_val = data["location"]["latitude"]
        longitude_val = data["location"]["longitude"]

    # Call API function
    result = get_weather_forecast(latitude=latitude_val, longitude=longitude_val, api_key=api_key_val)
    print(result)
