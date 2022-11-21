from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, kwargs={'http': [
        'Ковин Аскар Александрович',
        '16',
        'Программирование, эксперименты',
        '<a href="/about">about</a>',
        '<a href="/contacts">contacts</a>'
    ]}),
    path('about/', views.about),
    path('contacts/', views.contacts),
]
