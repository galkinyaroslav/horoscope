from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from zodiac.models import ZodiacSigns, SignHoroscope
from datetime import date

# Create your views here.
current_date = date.today()
zodiac_sign_pic_list = ['&#9800',
                        '&#9801',
                        '&#9802',
                        '&#9803',
                        '&#9804',
                        '&#9805',
                        '&#9806',
                        '&#9807',
                        '&#9808',
                        '&#9809',
                        '&#9810',
                        '&#9811', ]


def index(request):
    return render(request, 'zodiac/index.html', {'title': 'Главная страница',
                                                 'current_date': current_date,
                                                 'pics': zodiac_sign_pic_list, })


def zodiac_sign(request, sign):
    # if sign not in ZodiacSigns.object.all(): ToDo
    #     return redirect('home')
    return HttpResponse(f'<h1>TEAT SLUG</h1><p>{sign}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')
