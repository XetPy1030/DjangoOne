from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request, http):
    return HttpResponse('<br>'.join(http))

def about(request):
    http = [
        'Из Уфы, Башкирия',
        '4-5 успеваемость',
        'Люблю учиться'
    ]
    return HttpResponse('<br>'.join(http))

def contacts(request):
    http = [
        '<a href="https://github.com/XetPy1030">Git@XetPy1030</a>',
        '+79656650051',
        '<a href="https://t.me/XetPy">Telegram@XetPy</a>',
        '602 комната'
    ]
    return HttpResponse('<br>'.join(http))
