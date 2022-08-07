"""horoscope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dictionary import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls, name=""),
    path('contacts/', views.get_contacts),
    path('search_', views.get_search),
    # path('index/', views.get_home),
    path('', views.get_home),
    # path('news0/', views.get_news0),
    # path('news1/', views.get_news1),
    # path('news2/', views.get_news2),
    path('testcount/', views.get_test_count),
    path('whyitsite/', views.get_why),
    path('znak/', views.get_znak),
    path('', views.hello2),
    path('news0/', include([
        path('<int:sing_news>/', views.get_news0),

    # path('dictionary/', include('dictionary.urls')),
    # path('dictionary/', include([
    #     path('<int:sing_name>/', views.get_sign_name_number),
    #     path('<str:sing_name>/', views.get_sign_name),
        ])),
]

