#!/usr/bin/env python
# coding: utf-8

# In[1]:


from one_call_api_data import store_data
from one_call_api_data import one_api_weather_data
from one_call_api_data import write_weather_data_in_json_file
from one_call_api_data import convert_dict_to_df
from one_call_api_data import create_data
from config import city,lat,lon,key
import argparse
import time


# In[2]:


def start(lat,lon,city):
    
        data= one_api_weather_data(lat,lon,key)
        filename= write_weather_data_in_json_file(data)
        df=create_data(filename)
        store_data(df, city)
        
for i in range(0,len(lat)):
    start(lat[i],lon[i],city[i])

