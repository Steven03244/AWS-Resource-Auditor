"""TASK 5"""
import main_functionsqi
import requests
import folium
import json

"""TASK 6"""
def get_api_key(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data["aqi_api_key"]

my_aqi_api_key = get_api_key("api_key.json")

print("API key:", my_aqi_api_key)

"""TASK 7"""


def get_aqi_data(api_key):
    url = "http://api.airvisual.com/v2/nearest_city?key="
    url_aqi = url + api_key

    response = requests.get(url_aqi)
    data = response.json()

    with open("aqi.json", "w") as file:
        json.dump(data, file, indent=4)


get_aqi_data(my_aqi_api_key)


"""TASK 8"""
def generate_map(data_filename, zoom_start):
    aqi_data = main_functionsqi.read_from_file(data_filename)
    long, lat = aqi_data["data"]["location"]["coordinates"]
    m = folium.Map(location=[lat, long], zoom_start=zoom_start)
    folium.Marker(
        location=[lat, long],
        popup='AQI Station',
        icon=folium.Icon(color='green', icon='cloud')
    ).add_to(m)

    m.save("map.html")



generate_map("aqi.json", 10)


"""TASK 9"""
def display_aqi_info(data_filename):
    aqi_data = main_functionsqi.read_from_file(data_filename)

    tempC = aqi_data["data"]["current"]["weather"]["tp"]
    tempF = round((tempC * 9 / 5) + 32, 1)
    humid = aqi_data["data"]["current"]["weather"]["hu"]
    aqius = aqi_data["data"]["current"]["pollution"]["aqius"]

    if aqius <= 50:
        quality = "good:)"
    elif aqius <= 100:
        quality = "moderate"
    elif aqius <= 150:
        quality = "unhealthy for sensitive groups"
    elif aqius <= 200:
        quality = "unhealthy"
    else:
        quality = "very unhealthy:("

    print(
        f"The temperature is {tempC}ºC or {tempF}ºF, the humidity is {humid}%, and the index shows that the air quality is {quality}.")



display_aqi_info("aqi.json")

