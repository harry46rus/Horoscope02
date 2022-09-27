import json
import re

from dictionary.scrap01 import get_dates
# from scrap01 import get_dates
from dictionary.paths_01 import path_bd_json
# from paths_01 import path_bd_json

def head_title(num_news=0):
    print(num_news)
    path1 = f"{path_bd_json}numnews.json"
    with open(path1, 'r', encoding='utf-8') as f_five:
        count_news = json.load(f_five)

    sss =None
    date_num =get_dates()
    if 0 < num_news < 7:
        sss = date_num[num_news -1]
    # sing:[title,description,href,h3, кейворд,]
    title_dict = {
        0: [f'Новости Курска и Курской области сегодня на СоваБот.ру',
            f'"Узнавайте Главные новости Курска и Курской области на сегодня. Мы ежедневно '
            f'публикуем самую актуальную информацию. Репортажи, аналитика, происшествия, '
            f'ситуация на дорогах, новости политики, экономики, культуры и спорта.',
            'novosti-za-sem-dnej',
            f'Что произошло сегодня в Курске и Курской области.'
            f' Подборка из {count_news[num_news]} новостей',
            'новости курска, новости курска сегодня, курские новости, новости курской области',
             ],
        1: [f'Новости Курска и Курской области за {sss} на СоваБот.ру ',
            f'Что случилось {sss} в Курске и Курской области.Репортажи, аналитика, происшествия, '
            f'ситуация на дорогах, новости политики, экономики, культуры и спорта.',
            'kurskie-novosti-za-vchera',
            f'Что случилось {sss} в Курске и Курской области.'
            f' Подборка из {count_news[num_news]} новостей',
            'новости курска, новости курска сегодня, курские новости, новости курской области',
             ],
        2: [f'Новости Курска и Курской области за {sss} на СоваБот.ру ',
            f'Что случилось {sss} в Курске и Курской области.Репортажи, аналитика, происшествия, '
            f'ситуация на дорогах, новости политики, экономики, культуры и спорта.',
            'kurskie-novosti-za-vchera',
            f'Что случилось {sss} в Курске и Курской области.'
            f' Подборка из {count_news[num_news]} новостей',
            'новости курска, новости курска сегодня, курские новости, новости курской области',
            ],
        3: [f'Новости Курска и Курской области за {sss} на СоваБот.ру ',
            f'Что случилось {sss} в Курске и Курской области.Репортажи, аналитика, происшествия, '
            f'ситуация на дорогах, новости политики, экономики, культуры и спорта.',
            'kurskie-novosti-za-vchera',
            f'Что случилось {sss} в Курске и Курской области.'
            f' Подборка из {count_news[num_news]} новостей',
            'новости курска, новости курска сегодня, курские новости, новости курской области',
            ],
        4: [f'Новости Курска и Курской области за {sss} на СоваБот.ру ',
            f'Что случилось {sss} в Курске и Курской области.Репортажи, аналитика, происшествия, '
            f'ситуация на дорогах, новости политики, экономики, культуры и спорта.',
            'kurskie-novosti-za-vchera',
            f'Что случилось {sss} в Курске и Курской области.'
            f' Подборка из {count_news[num_news]} новостей',
            'новости курска, новости курска сегодня, курские новости, новости курской области',
            ],
        5: [f'Новости Курска и Курской области за {sss} на СоваБот.ру ',
            f'Что случилось {sss} в Курске и Курской области.Репортажи, аналитика, происшествия, '
            f'ситуация на дорогах, новости политики, экономики, культуры и спорта.',
            'kurskie-novosti-za-vchera',
            f'Что случилось {sss} в Курске и Курской области.'
            f' Подборка из {count_news[num_news]} новостей',
            'новости курска, новости курска сегодня, курские новости, новости курской области',
            ],
        6: [f'Новости Курска и Курской области за {sss} на СоваБот.ру ',
            f'Что случилось {sss} в Курске и Курской области.Репортажи, аналитика, происшествия, '
            f'ситуация на дорогах, новости политики, экономики, культуры и спорта.',
            'kurskie-novosti-za-vchera',
            f'Что случилось {sss} в Курске и Курской области.'
            f' Подборка из {count_news[num_news]} новостей',
            'новости курска, новости курска сегодня, курские новости, новости курской области',
            ],
        7: [f'Анонсы новостей Курска и Курской области сегодня на СоваБот.ру',
            f'Что будет, чего ждать жителям Курска и Курской области?'
            f'Будущие события мероприятия, планы, объявления для на предстоящие дни. Подборка из '
            f'{count_news[num_news]} новостей',
            'vse-anonsy-kurskih-sobytij',
            f'Что произойдет в Курске и области в ближайшее время. Подборка из'
            f' {count_news[num_news]} новостей',
            'когда будет, когда наступит, когда произойдет, сколько ждать'
            ],
        8: [f'Происшествия в Курске и Курской области сегодня на СоваБот.ру',
            f'Что случилось в Курске и области. ДТП,Пожары,'
            f'Случаи мошенничества, Кражи, Судебные дела, Специальная Военная Операция на Украине. '
            f'Подборка из {count_news[num_news]} новостей',
            'proisshestviya-v-kurske-i-oblasti',
            f'Что случилось  сегодня в Курске и Курской области. '
            f'Подборка из {count_news[num_news]} новостей',
            ],
        9: [f'Новости ОБЩЕСТВО: в Курске и Курской области сегодня на СоваБот.ру',
            f'Что было в Курске и области: Культура,ЖКХ, Медицина, Спорт,Образование, Медицина,'
            f'Экономика ,'
            f'ЖКХ. Подборка из {count_news[num_news]} новостей',
            'novosti-obschestva-v-kurske-i-oblasti',
            'Что произошло сегодня в Курске и Курской области. '
            f'Подборка из {count_news[num_news]} новостей'
            ],
        10: [f'Новости ЖКХ: в Курске и Курской области сегодня на СоваБот.ру',
            f'Самые свежие новости ЖКХ сегодня Курска и Курской области на сегодня. '
            f'Подборка из {count_news[num_news]} новостей',
            'novosti-zhkh-po-kursku-i-oblasti',
            f'Что произошло сегодня в ЖКХ Курска и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        11: [f'Новости Спорта в Курске и Курской области сегодня на СоваБот.ру',
            f'Самые свежие новости спорта Курска и Курской области на сегодня.'
            f' Подборка из {count_news[num_news]} новостей',
             'sportivnye-sobytiya-v-kurske-i--oblasti',
             f'Спортивные события Курска и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        12: [f'Новости Медицины в Курске и Курской области сегодня на СоваБот.ру',
            f'Самые свежие новости медицины Курска и Курской области на сегодня.'
            f' Подборка из {count_news[num_news]} новостей',
             'novosti-meditsiny-v-kurske-i-oblasti',
             f'Новости медицины Курска и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        13: [f'Новости Образования в Курске и Курской области сегодня на СоваБот.ру',
            f'Самые свежие новости образования сегодня Курска и Курской области.'
            f' Подборка из {count_news[num_news]} новостей',
             'novosti-obrazovaniya-kurska-i-oblasti',
             f'Новости образования Курска и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        14: [f'Новости Экономики в Курске и Курской области сегодня на СоваБот.ру',
            f'Самые свежие новости экономики  Курска и Курской области на сегодня.'
            f' Подборка из {count_news[num_news]} новостей',
             'novosti-ekonomiki-kurska-i-oblasti',
             f'Новости экономики Курска и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        15: [f'Новости Культуры в Курске и Курской области сегодня на СоваБот.ру',
            f'Самые свежие новости культуры Курска и Курской области на сегодня.'
            f' Подборка из {count_news[num_news]} новостей',
             'kulturnye-novosti-kurska-i-oblasti',
             f'Новости культуры Курска и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        16: [f'Последние ДТП в Курске и Курской области сегодня на СоваБот.ру',
            f'Самые последние ДТП  Курска и Курской области на сегодня. Подборка из'
            f' {count_news[num_news]} новостей',
             'dorozhnye-proisshestviya-kurska-i-oblasti',
             f'ДТП в Курске и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        17: [f'Последние ПОЖАРЫ в Курске и Курской области сегодня на СоваБот.ру ',
            f'Самые последние пожары Курска и Курской области на сегодня. '
            f'Подборка из {count_news[num_news]} новостей',
             'pozhary-kurska-i-oblasti',
             f'Пожары в Курске и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        18: [f'Случаи мошенничества в Курске и Курской области сегодня на СоваБот.ру',
            f'Самые последние новости о мошенничестве Курска и Курской области на сегодня. '
            f'Подборка из {count_news[num_news]} новостей',
             'moshenniki-v-kurske-i-oblasti',
             f'Мошенники в Курске и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        19: [f'КРАЖИ: сводка новостей из Курске и Курской области сегодня на СоваБот.ру',
            f'Самые свежие новости о кражах Курска и Курской области на сегодня. '
            f'Подборка из {count_news[num_news]} новостей',
             'krazhi-v-kurske-i-oblasti',
             f'Кражи в Курске и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        20: [f'Суды в Курске и Курской области сегодня на СоваБот.ру',
            f'Самые последние новости о судах  Курска и Курской области на сегодня.'
            f' Подборка из {count_news[num_news]} новостей',
             'sudebnye-novosti-kurska-i-oblasti',
             f'Суды в Курске и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        21: [f'СПЕЦОПЕРАЦИЯ НА УКРАИНЕ И КУРСКОЙ ОБЛАСТИ ',
            f'Самые последние новости о Специальной военной операции  на Украине и Курской области '
            f'насегодня. Подборка из {count_news[num_news]} новостей',
             'spetsialnaya-voennaya-operatsiya',
             f'Что произошло на Украине и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        22: [f'Анонсы событий на сегодня в Курске и Курской области на СоваБот.ру',
             f'Самые свежие анонсы Курска и Курской области на сегодня.'
            f' Подборка из {count_news[num_news]} новостей',
            'kurskie-anonsy-na-segodnya',
             f'Какие события ожидают Курск и Курскую область. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        23: [f'Анонсы событий на завтра в Курске и Курской области на СоваБот.ру',
            f'Самые свежие анонсы событий на завтра Курска и Курской области.'
            f' Подборка из {count_news[num_news]} новостей',
             'kurskie-anonsy-na-zavtra',
             f'Что произойдет завтра в Курске и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        24: [f'Анонсы событий на послезавтра в Курске и Курской области на СоваБот.ру',
            f'Самые свежие анонсы событий на послезавтра Курска и Курской области. '
            f'Подборка из {count_news[num_news]} новостей',
             'anonsy-kurskih-sobytij-na-poslezavtra',
             f'Что произойдет послезавтра в Курске и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        25: [f'Анонсы событий в Курске и Курской области на СоваБот.ру',
            f'Самые свежие анонсы событий Курска и Курской области. '
            f'Подборка из {count_news[num_news]} новостей',
             'anonsy-kurskih-sobytij-na-zavtra',
             f'Что произойдет в Курске и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
        26: [f'Объявления и информация по Курску и Курской области на СоваБот.ру',
            f'Самые свежие объявления и информация по Курску и Курской области. '
            f'Подборка из {count_news[num_news]} новостей',
             'obyavleniya-po-kursku-i-oblasti',
             f'Чего ждать в Курске и Курской области. Подборка из'
             f' {count_news[num_news]} новостей'
             ],
    }

    titl =title_dict[num_news][0]
    descrip = title_dict[num_news][1]
    # link_0= title_dict[num_news][2]
    hh3 = title_dict[num_news][3]
    # count_n = title_dict[num_news][1]
    return titl,sss,descrip,hh3

def html_date(link_='novosti-za-sem-dnej'):
    # sss=0
    # count_news={}
    # sing_news=0
    link_dict = {'novosti-za-sem-dnej': 0,
                'kurskie-novosti-za-vchera': 1,
                'kurskie-novosti-za-pozavchera':2,
                'kurskie-novosti-tri-dnya-nazad': 3,
                'kurskie-novosti-chetyre-dnya-nazad': 4,
                'kurskie-novosti-pyat-dnej-nazad': 5,
                'kurskie-novosti-shest-dnej-nazad': 6,
                'vse-anonsy-kurskih-sobytij': 7,
                'proisshestviya-v-kurske-i-oblasti': 8,
                'novosti-obschestva-v-kurske-i-oblasti': 9,
                'novosti-zhkh-po-kursku-i-oblasti': 10,
                'sportivnye-sobytiya-v-kurske-i--oblasti': 11,
                'novosti-meditsiny-v-kurske-i-oblasti': 12,
                'novosti-obrazovaniya-kurska-i-oblasti': 13,
                'novosti-ekonomiki-kurska-i-oblasti': 14,
                'kulturnye-novosti-kurska-i-oblasti': 15,
                'dorozhnye-proisshestviya-kurska-i-oblasti': 16,
                'pozhary-kurska-i-oblasti': 17,
                'moshenniki-v-kurske-i-oblasti': 18,
                'krazhi-v-kurske-i-oblasti': 19,
                'sudebnye-novosti-kurska-i-oblasti': 20,
                'spetsialnaya-voennaya-operatsiya': 21,
                'kurskie-anonsy-na-segodnya': 22,
                'kurskie-anonsy-na-zavtra': 23,
                'anonsy-kurskih-sobytij-na-poslezavtra': 24,
                'anonsy-kurskih-sobytij-na-zavtra': 25,
                'obyavleniya-po-kursku-i-oblasti': 26}

    list_link = list(link_dict)
    num_news=link_dict[link_]
    return num_news, list_link

# head_title(num_news=0)
print(html_date(link_='novosti-za-sem-dnej'))

def count_word(numberGLdate=0):
    common_list=[]
    dict_words={}
    dict_words1={}
    path2 = f"{path_bd_json}GLdate{numberGLdate}.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    titls_news = list(json_data_news)
    for i in titls_news:
        for j in i.replace('.', '').split():

            common_list.append(j)
    # print(common_list)
    print("Количество слов в обработке",len(common_list))
    for x in common_list:
        score=0
        if len(x)>4:
            for y in common_list:
                if x[:-1] == y[:-1] or x[:-1] == y[:] or x[:] == y[:-1]:
                    score+=1
            dict_words1[x[:-1]] = score,x

    key_except = r'курс[к]?|област|челове|рубле|мужчи[н]?|женщин|январ|феврал|мар|апрел|июн|июл|ььь\
            |авгус|октябр|ноябр|сентябр|декабр|росси|район|жител|сутк|куря[н]?'
    n=2# не включать в результат слова которые повторяются "n" и меньше раз
    for title, y in dict_words1.items():
        result = re.findall(key_except, title.lower())
        if result:
            pass
        else:
            if y[0]>n:
                dict_words[title]=y
            # print(y[0])
    # print(dict_words)
    sorted_dict = {}
    sorted_keys = sorted(dict_words, key=dict_words.get, reverse=True)
    # print('**',sorted_keys)
    # print('--',len(sorted_keys))

    for w in sorted_keys:
        sorted_dict[w] = dict_words[w]

    #тема дня частотное слово "новости о мобилизации"
    # print(len(sorted_dict))
    for i,y in sorted_dict.items():
        print(i,y)

def search_news(word,numberGLdate=0):
    path2 = f"{path_bd_json}GLdate{numberGLdate}.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    search_dict={}

    for i, y in json_data_news.items():
        if word in i:
            search_dict[i] = y
    print(len(search_dict))
    for i,y in search_dict.items():
        print(i,y)

# count_word(0)
# search_news('мобилизаци',3)
