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
from dictionary.seo_logics import head_title,html_date
from django.core.paginator import Paginator

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


# def get_sign_name(request):#, sing_name: str):
#     # description = zodiac_dict.get(sing_name, None)
#     # data = {
#     #     "description_zodiac": description,
#     #     "sign_": sing_name.upper(),
#     #     # "my_int": 123,
#     #     # "my_float": 25.3,
#     #     # "my_list": [1, 2, 3],
#     #     # "my_dict": {"name": "Piter"},
#     #     # "my_class": Person("Jack", 50),
#
#     # }
#     return render(request, 'horoscop.html')#, context=data)

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
    num_news = 99




    data = {

        'num_news': num_news,
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

    if sing_news < 27:
        hour_= datetime.strftime(datetime.now(), "%H")
        days_= datetime.strftime(datetime.now(), "%d")
        # hour= datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        fff, numnews = scrap(sing_news)
        usd_ = get_USD()
        # number_news = len(fff)
        for date_, value in usd_.items():
            dddate, usd, eur = date_, value[1], value[3]
        # =====================================================
        titl,sss,descrip =head_title(sing_news)
        # sss=0
        date_num=get_dates()
        # if 0 < sing_news < 7:
        #     sss = date_num[sing_news-1]


        data = {
            'sing_news': sing_news,
            'numnews': numnews,
            'sss': sss,
            'date_': dddate,
            'usd': usd,
            'eur': eur,
            "titl": titl,
            # 'count_n':count_n,
            'descrip':descrip,
            'news_dict': fff,
            "time": hour_,
            "day_": days_,
            "date_num": date_num}

        return render(request, "news0.html", context=data)
    else:
        return render(request, "error404.html")

def get_sign_name(request, sing_news: str):
    # перевод ссылки в число
    num_news,list_link = html_date(sing_news)
    # html_date(link_='novosti-za-sem-dnej')
    # print(num_news,list_link)

    if num_news < 27:
        hour_ = datetime.strftime(datetime.now(), "%H")
        days_ = datetime.strftime(datetime.now(), "%d")
        # hour= datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        fff, numnews = scrap(num_news)
        usd_ = get_USD()
        # number_news = len(fff)
        for date_, value in usd_.items():
            dddate, usd, eur = date_, value[1], value[3]
        # =====================================================
        titl,sss,descrip,hh3,key_word = head_title(num_news)
        # sss=0
        date_num = get_dates()
        # if 0 < sing_news < 7:
        #     sss = date_num[sing_news-1]
        pict = f'cat.jpg'  # f'dog.jpg'f'church.jpg'#

        # contact_list = fff

        contact_list = list(fff)
        # contact_list = (fff.items())[0]
        paginator = Paginator(contact_list, 40)
        # print('fff',fff)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {
            # 'menu': menu,:
            'page_obj': page_obj,
            'num_news': num_news,
            'numnews': numnews,
            'sss': sss,
            'hh3': hh3,
            'date_': dddate,
            'usd': usd,
            'eur': eur,
            'pict': pict,
            "titl": titl,
            'key_word':key_word,
            'list_link':list_link,
            'descrip': descrip,
            'news_dict': fff,
            "time": hour_,
            "day_": days_,
            "date_num": date_num}

        return render(request, "news0.html", context=data)
    else:
        return render(request, "error404.html")

def get_home(request):
    hour_ = datetime.strftime(datetime.now(), "%H")
    days_ = datetime.strftime(datetime.now(), "%d")
    # hour= datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    num_news = 0
    fff, numnews = scrap(0)
    usd_ = get_USD()

    for date_, value in usd_.items():
        dddate, usd, eur = date_, value[1], value[3]

    titl, sss, descrip, hh3,key_word = head_title(0)
    date_num = get_dates()

    contact_list = list(fff)
    paginator = Paginator(contact_list, 40)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'page_obj': page_obj,
        'num_news': num_news,
        'numnews': numnews,
        'sss': sss,
        'hh3': hh3,
        'date_': dddate,
        "titl": titl,
        'key_word': key_word,
        'descrip': descrip,
        'usd': usd,
        'eur': eur,
        'news_dict': fff,
        "time": hour_,
        "day_": days_,
        "date_num": date_num}
    return render(request, "news0.html", context=data)


def handle_404(request, exception):
    fff, numnews = scrap('0')
    usd_ = get_USD()
    for date_, value in usd_.items():
        dddate, usd, eur = date_, value[1], value[3]
    date_num = get_dates()
    sing_news = 100

    data = {
        'sing_news': sing_news,
        'numnews': numnews,
        'date_': dddate,
        'usd': usd,
        'eur': eur,
        'news_dict': fff,

        "date_num": date_num}
    return render(request, 'error404.html',context=data)


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



def hello2(request):
    pass
    return HttpResponseRedirect("https://www.djangoproject.com")


# get_sign_name(request,'kurskie-novosti-tri-dnya-nazad')
# print(f'C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\static\\images{{pict}}')