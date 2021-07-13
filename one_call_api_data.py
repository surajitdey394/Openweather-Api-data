#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import json
import requests
import sqlite3

one_api_file='C:/Users/surajit/Desktop/one_api_file.json'
city='boston'

def one_api_weather_data(lat,lon,key):
    
    city_api_endpoint = "http://api.openweathermap.org/data/2.5/onecall?"
    json_data = requests.get(city_api_endpoint + "lat=" +str(round(lat,2)) +"&lon=" + str(round(lon,2)) + "&appid="+
                                 'a640b5c91fa6851abedf4ba3dcf3b677').json()
        
    print("..........Getting one call api data from OpenWeatherMap.org..........")
    return json_data

def write_weather_data_in_json_file(json_data):

    name = str(json_data['hourly'][1]['dt'])
    one_api_file = r"data_cache/%s.json" % name
    
    with open('one_api_file.json', 'w') as f:
        json.dump(json_data, f)
    print('Created the json file')
    return one_api_file

def convert_dict_to_df(one_api_file):
    
    path_to_json= 'C:/Users/surajit/Desktop/one_api_file.json'
    with open(path_to_json, 'r') as data_file:
        json_one_api_load_file = json.load(data_file)
    
    return pd.json_normalize(json_one_api_load_file['hourly'])

def create_data(one_api_file):
    
    df_one_api_list= convert_dict_to_df(one_api_file)
    df_one_api_list_proccessed = df_one_api_list.drop(['dew_point','uvi','clouds','visibility','weather','pop','rain.1h'],axis=1)
    return df_one_api_list_proccessed.set_index("dt")

def store_data(df,city):
    
   
    connection = sqlite3.connect('One_Api_Weather.db', uri=True)
    print("..........Connection with database established ..........")
    connection.cursor()
    
    returned_connection = connection
    df.to_sql(city, returned_connection, if_exists='append', index=True)
    print("Uploaded!")
   
    connection.commit()
    connection.close()

