import pandas as pd
import json
import requests
import sqlite3

def current_weather_data(city,key,units):
    city_api_endpoint = "https://api.openweathermap.org/data/2.5/weather?q="
    json_data = requests.get(city_api_endpoint + city + "&appid=" + key + "&units="+ units).json()
    print("Getting current weather data from OpenWeatherMap.org..........")
    return json_data


def write_weather_data_in_json_file(city,json_data):

    name = city + str(json_data['dt'])
    filename = r"data_cache/%s.json" % name
    
    with open('filename.json', 'w') as f:
        json.dump(json_data, f)
    print('Created the json file')   
    return filename
    
def convert_dict_to_df(filename):
    
    path_to_json= 'C:/Users/surajit/Desktop/filename.json'
    with open(path_to_json, 'r') as data_file:
        json_load_file = json.load(data_file)
    
    return pd.json_normalize(json_load_file['list'])

def create_data(filename):
    
    df_list_data=convert_dict_to_df(filename)
    df_list_data_proccessed= df_list_data.drop(["weather","pop","dt_txt","rain.3h","sys.pod","main.sea_level","main.grnd_level","main.humidity","main.temp_kf","main.pressure"],axis=1)
    
    '''rename the columns'''
    df_list_data_proccessed= df_list_data_proccessed.rename(columns={'dt':'dt_id','main.temp': 'temperature','main.feels_like': 'apparent_temperature', 'main.temp_min': 'min_temeprature', 'main.temp_max': 'max_temeperature', 'clouds.all': 'clouds', 'wind.speed': 'wind_speed', 'wind.deg': 'wind_deg','wind.gust': 'wind_gust'})
    return df_list_data_proccessed.set_index("dt_id")
    
def store_data(df, city):
    
    connection = sqlite3.connect('CurrentWeather.db', uri=True)
    print("..........Connection with database established ..........")
    connection.cursor()
    
    returned_connection = connection
    df.to_sql(city, returned_connection, if_exists='append', index=True)
    print("Uploaded!")
    
    connection.commit()
    connection.close()
    
if __name__ == "__current_weather_main__":
    import doctest
    doctest.testmod()