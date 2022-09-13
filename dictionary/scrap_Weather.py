import requests
import json
from paths_01 import path_bd_json
# from bs4 import BeautifulSoup

# import schedule
# import pickle
# import datetime
# import threading

def weather():
    link ='http://api.openweathermap.org/data/2.5/find?q=Kursk&type=like&APPID=b8b36042f104978b92e324f0d0886702'
    s_city = "Kursk,RU"
    city_id = 538560
    appid = "b8b36042f104978b92e324f0d0886702"

    weather_dict={}
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
    #     print("conditions:", data['weather'][0]['description'])
    #     print("temp:", data['main']['temp'])
    #     print("temp_min:", data['main']['temp_min'])
    #     print("temp_max:", data['main']['temp_max'])
    except:
        print("Exception (weather):")
        pass
    print('=========================================================')
    month_ = {
        '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая',
        '06': 'июня',
        '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября',
        '12': 'декабря'
    }
    for i in range(40):
        time =data['list'][i]['dt_txt'][-8:]#:0]
        # print(time)
        if time=='00:00:00':
            # print('ночь',data['list'][i]['dt_txt'])
            day = data['list'][i]['dt_txt'][-11:-9]
            month_n = month_[data['list'][i]['dt_txt'][-14:-12]]
            print(f'ночью {day} {month_n}')
            night = f'ночью {day} {month_n}'

            print('температура',round(data['list'][i]['main']['temp']),'°C')
            temper = round(data['list'][i]['main']['temp'])
            if temper>0:
                temper = f'+{temper}°C'
            else:
                temper = f'{temper}°C'
            print('давление',round(int(data['list'][i]['main']['pressure'])/1.333),'мм рт.ст')
            press = round(int(data['list'][i]['main']['pressure'])/1.333)
            press = f'{press} мм рт.ст'

            print('влажность',data['list'][i]['main']['humidity'],'%')
            humid= data['list'][i]['main']['humidity']
            humid= f'{humid} %'
            print('осадки',data['list'][i]['weather'][0]['description'])
            rain = data['list'][i]['weather'][0]['description']
            print('ветер',data['list'][i]['wind']['speed'],'м/с')
            wind = data['list'][i]['wind']['speed']
            wind = f'{wind} м/с'
            print('=============================')
            weather_dict[night]=[temper,press,humid,rain,wind]
        elif time == '12:00:00':
            day = data['list'][i]['dt_txt'][-11:-9]
            month_n = month_[data['list'][i]['dt_txt'][-14:-12]]
            print(f'днем {day} {month_n}')
            day=f'днем {day} {month_n}'
            print('температура', round(data['list'][i]['main']['temp']),'°C')
            temper = round(data['list'][i]['main']['temp'])
            if temper > 0:
                temper = f'+{temper}°C'
            else:
                temper = f'{temper}°C'
            print('давление',round(int(data['list'][i]['main']['pressure'])/1.333),'мм рт.ст')
            press = round(int(data['list'][i]['main']['pressure']) / 1.333)
            press = f'{press} мм рт.ст'
            print('влажность', data['list'][i]['main']['humidity'],'%')
            humid = data['list'][i]['main']['humidity']
            humid = f'{humid} %'
            print('осадки', data['list'][i]['weather'][0]['description'])
            rain = data['list'][i]['weather'][0]['description']
            print('ветер', data['list'][i]['wind']['speed'],'м/с')
            wind = data['list'][i]['wind']['speed']
            wind = f'{wind} м/с'
            print('=============================')

            weather_dict[day]=[temper,press,humid,rain,wind]



    path1 = f"{path_bd_json}Weath_date.json"
    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(weather_dict, file, ensure_ascii=False, indent=0)

weather()