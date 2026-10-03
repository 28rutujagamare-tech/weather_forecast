from django.urls import path
from . import views 
urlpatterns=[
    path('city/',views.weather,name='city'),
]
