# Openweather-Api-data

1.Provide the key or any city name in the config.py file

2. fetch data from Current Weather API:
      1. Run current_weather_main.py 
      2. current-weather_data.py script contains the transformation of raw data and saving it into CurrentWeather database. 
3. Fetch data from One Call API:
      1. Run one_api_main.py
      2. one_call_api.py script contains the transformation of raw data and saving it into OneApiWeather database.
4. To view the database, I used tableau tool to see the table format of the data in the database.
      1. Open tableau select other ODBC connection.
      2. Select sqlite3 ODBC server from the driver menu.
      3. Browse the database in your local machine and it will load the database.
5. For the visualization- open the link https://prod-apnortheast-a.online.tableau.com/#/site/jupyter/collections/0a7e8c26-4b67-441c-8354-fa94cb79e630?:origin=card_share_link

![image](https://user-images.githubusercontent.com/24209142/125498355-30ed0aae-9ef6-4457-96f9-bc1b777450ce.png)
