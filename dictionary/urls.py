from django.urls import path, include
from dictionary import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('dictionary/', include('dictionary.urls')),
    # path('dictionary/', include('dictionary.urls')),# path('admin/', admin.site.urls),
    # # path('dictionary/', include('dictionary.urls')),
    # path('<int:sing_name>/', views.get_sign_name_number),

    path('<str:sing_name>/', views.get_sign_name),
    # path('dictionary/<str:sing_name>/', views.get_sign_name),
    # path('contacts/', views.get_contacts),
    # path('index/', views.get_home),
    # path('znak/', views.get_znak),
]


