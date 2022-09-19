from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from dataclasses import dataclass
from dictionary.loggics import search_words
from dictionary.testcount import tcounter
from dictionary.scrap01 import scrap,get_dates#,scrap1,scrap2
from dictionary.read_USD import get_USD
from datetime import datetime

# def leo(request):
#     return HttpResponse("Hello, Dictionary!!!")
#
#
# def scorpio(request):
#     return HttpResponse("Hello, BOOK!!!")


# def get_sign_name(request, sing_name):
#     if sing_name == 'leo':
#         return HttpResponse(f"             -------HEllo, BOOK   {sing_name.upper()}!!!")


zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
     }


# def get_sign_name(request, sing_name: str):
#     description = zodiac_dict.get(sing_name, None)
#     if description:
#         return HttpResponse(f'<h1>{description}/</h1><br>'
#                              f'<a href="/index"> =Home= </a>')
#     else:
#         if sing_name=="gen":
#             return redirect("https://www.djangoproject.com")
#         else:
#
#             return HttpResponseNotFound(f"Неизвестный знак--{sing_name.upper()}!!!")

# @dataclass
# class Person:
#     name: str
#     age: str
#
#     def __str__(self):
#         return f"This is {self.name}"


def get_sign_name(request):#, sing_name: str):
    # description = zodiac_dict.get(sing_name, None)
    # data = {
    #     "description_zodiac": description,
    #     "sign_": sing_name.upper(),
    #     # "my_int": 123,
    #     # "my_float": 25.3,
    #     # "my_list": [1, 2, 3],
    #     # "my_dict": {"name": "Piter"},
    #     # "my_class": Person("Jack", 50),

    # }
    return render(request, 'horoscop.html')#, context=data)


def get_sign_name_number(request, sing_name: int):
    zodiacs = list(zodiac_dict)
    if sing_name > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный знак зодиака--{sing_name}!!!")
    name_zodiac = zodiacs[sing_name - 1]
    return HttpResponseRedirect(f'/dictionary/{name_zodiac}')


def get_contacts(request):
    return render(request, "contacts.html")


def get_search(request):
    # print("search=",search)
    return render(request, "search_.html")


def get_home1(request):
    return render(request, "index.html")

def get_why(request):
    days_ = datetime.strftime(datetime.now(), "%d")
    fff, numnews = scrap('0')
    usd_ = get_USD()
    # number_news = len(fff)
    for date_, value in usd_.items():
        dddate, usd, eur = date_, value[1], value[3]

    date_num = get_dates()
    sing_news = 99
    data = {
        'sing_news': sing_news,
        'numnews': numnews,
        # 'number_news': number_news,
        'date_': dddate,
        'usd': usd,
        'eur': eur,
        'news_dict': fff,
        "day_": days_,
        "date_num": date_num}

    return render(request, "whyitsite.html", context=data)




def get_news0(request, sing_news: int):
    hour_= datetime.strftime(datetime.now(), "%H")
    days_= datetime.strftime(datetime.now(), "%d")
    # hour= datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    fff, numnews = scrap(sing_news)
    usd_ = get_USD()
    # number_news = len(fff)
    for date_, value in usd_.items():
        dddate, usd, eur = date_, value[1], value[3]

    date_num=get_dates()

    data = {
        'sing_news': sing_news,
        'numnews': numnews,
        # 'number_news': number_news,
        'date_': dddate,
        'usd': usd,
        'eur': eur,
        'news_dict': fff,
        "time": hour_,
        "day_": days_,
        "date_num": date_num}
    return render(request, "news0.html", context=data)

def get_home(request):
    hour_ = datetime.strftime(datetime.now(), "%H")
    days_ = datetime.strftime(datetime.now(), "%d")
    # hour= datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    sing_news = 0
    fff, numnews = scrap(sing_news)
    usd_ = get_USD()

    for date_, value in usd_.items():
        dddate, usd, eur = date_, value[1], value[3]

    date_num = get_dates()

    data = {
        'sing_news': sing_news,
        'numnews': numnews,

        'date_': dddate,
        'usd': usd,
        'eur': eur,
        'news_dict': fff,
        "time": hour_,
        "day_": days_,
        "date_num": date_num}
    return render(request, "news0.html", context=data)



# def get_news1(request):
#     hour_= datetime.strftime(datetime.now(), "%H")
#     days_= datetime.strftime(datetime.now(), "%d")
#     # hour= datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
#     fff = scrap1()
#     usd_ = get_USD()
#     number_news = len(fff)
#     for date_, value in usd_.items():
#         dddate, usd, eur = date_, value[1], value[3]
#
#     data = {
#         'number_news': number_news,
#         'date_': dddate,
#         'usd': usd,
#         'eur': eur,
#         'news_dict': fff,
#         "time": hour_,
#         "day_": days_,}
#     return render(request, "news1.html", context=data)
#
# def get_news2(request):
#     hour_= datetime.strftime(datetime.now(), "%H")
#     days_= datetime.strftime(datetime.now(), "%d")
#     # hour= datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
#     fff = scrap2()
#     usd_ = get_USD()
#     number_news = len(fff)
#     for date_, value in usd_.items():
#         dddate, usd, eur = date_, value[1], value[3]
#
#     data = {
#         'number_news': number_news,
#         'date_': dddate,
#         'usd': usd,
#         'eur': eur,
#         'news_dict': fff,
#         "time": hour_,
#         "day_": days_,}
#     return render(request, "news2.html", context=data)

# list_s=[i*6 for i in range(1,10)]



def get_test_count(request):
    qq = []
    rezz = None
    contact1 = None
    contact2 = None
    contact3 = None
    namefile = None

    if request.method == 'POST':
        # qq.append(request.POST.get('question1'))
        # qq.append(request.POST.get('question2'))

        for i in range(1,201):
            quest_=f'question{i}'
            qq.append(request.POST.get(quest_))

        contact1=request.POST.get('contact_field_0')
        contact2=request.POST.get('contact_field_1')
        contact3=request.POST.get('contact_field_2')
        sex=request.POST.get('sex')

        dictq = {}
        for x in range(1, 201):
            #     print(x)
            dictq[x] = qq[x - 1]

        rezz,namefile =  tcounter(dictq,contact1,contact2,contact3,sex)



    context2 = {
        # 'zz': qq,
        'zz': rezz,
        'cc1':contact1,
        'cc2':contact2,
        'cc3':contact3,
        'nmf':namefile,

    }
    # return render(request, "znak.html", context=context1)cd
    # return render(request, "horoscop.html", context=context2)
    return render(request, "testcount.html", context=context2)


def get_znak(request):
    # def get_search(request):
    ff = []
    zapros = None
    aa=None
    if request.method == 'POST':
        zapros = request.POST.get('city')
        # ff=loggics(zapros)
        # base_='all_hcob.data'
        ff, aa = search_words(zapros)
    context1 = {
        "temp": ff,
        'zapros': zapros,
        'aa': aa
    }
    # return render(request, "znak.html", context=context1)cd
    return render(request, "search_.html", context=context1)


# def hello(request):
#     # today = datetime.datetime.now().date()
#     # daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#     return redirect("https://www.djangoproject.com")
# # Create your views here.
#
#
def hello2(request):
    pass
    return HttpResponseRedirect("https://www.djangoproject.com")

# def myView(request):
#     context = {}
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         api_address = 'http://api.openweathermap.org/data/2.5/weather? appid=KEY&q='
#         url = api_address + city
#         json_data = requests.get(url).json()
#         kelvin = json_data['main']['temp']
#         context['temperature'] = round(kelvin - 273.15, 0)
#     render(request, 'template_name.html', context)
