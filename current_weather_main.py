#!/usr/bin/env python
# coding: utf-8

# In[4]:


from current_weather_data import store_data
from current_weather_data import current_weather_data
from current_weather_data import write_weather_data_in_json_file
from current_weather_data import convert_dict_to_df
from current_weather_data import create_data
#from current_weather_data import 
import argparse
import time


# In[5]:


city = [city for city in input("Enter city name: ").split(",")]
length=len(city)
parser = argparse.ArgumentParser()

parser.add_argument("--frequency", default=10000, type=int, help="How often does the program run in seconds")
args, unknown = parser.parse_known_args()

for i in range(0,length):
    def start():
    
        data= current_weather_data(city[i],'a640b5c91fa6851abedf4ba3dcf3b677','metrics')
        filename= write_weather_data_in_json_file(city[i],data)
        df=create_data(filename)
        store_data(df, city[i])
        
#while True:
#    start()
#    time.sleep(args.frequency)


# In[ ]:




