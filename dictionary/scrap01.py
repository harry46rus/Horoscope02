import datetime
import json





def scrap(day_ago):
    """Выборка последнего json-файла для показа на сайте и конвертация в обычный словарь"""

    # #чтение и конвертация в обычный словарь
    path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
            f"\\GLdate{day_ago}.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\numnews.json"

    with open(path1, 'r', encoding='utf-8') as f_five:
        numnews = json.load(f_five)

    return json_data_news, numnews

def get_dates():
    """дает даты(день, месяц, год) дней -  вчера , позавчера, ..., 6 дней назад"""

    date_format = '%d.%m.%Y'
    day1 = datetime.datetime.now()
    list_days= []
    for i in range(1, 7):
        fd=day1 - datetime.timedelta(days=i)
        list_days.append(fd.strftime(date_format))

    return list_days


