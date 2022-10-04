import datetime
import json
import time

from paths_01 import path_bd_json
# path_bd_json=f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\"

def arh_news_count_json():
    """записывает в архивную папку 'bd_json/arh_news/'  файл 'arh_news_count' из
    файла numnews.json , поставить в Cron время выполнения этого
      скрипта примерно 23:00. Здесь отражено изменение количества новостей по дням в numnews.json"""
    arh_news_dict={}

    path2 = f"{path_bd_json}numnews.json"
    path1 = f"{path_bd_json}arh_news\\arh_news_count.json"#/вместо\\

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)
    print(json_data_news)
    try:
        with open(path1, 'r', encoding='utf-8') as f_five:
            arh_news_dict = json.load(f_five)
        print(arh_news_dict)
    except:
        pass

    now = datetime.datetime.now()

    dtime_= str(now)[:10]

    print(dtime_)
    arh_news_dict[dtime_] = json_data_news

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(arh_news_dict, file, ensure_ascii=False, indent=None)#indent=None-не переносит
        # на новую строку, indent=0 переносит на новую строку

    # print(json_data_news)


arh_news_count_json()
