from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from zodiac.models import ZodiacSign, SignHoroscope
from datetime import date
from bs4 import BeautifulSoup
import requests

# Create your views here.
current_date = date.today()


def index(request):
    zodiac_signs = ZodiacSign.objects.all().order_by('pk')
    return render(request, 'zodiac/index.html', {'title': 'Главная страница',
                                                 'current_date': current_date,
                                                 'zodiac_signs': zodiac_signs}, )


def sign_horoscope(request, sign_slug):
    sign = ZodiacSign.objects.get(sign_name=f'{sign_slug}'.capitalize())
    try:
        sign_hor = SignHoroscope.objects.get(sign_id__sign_name=f'{sign_slug}'.capitalize(),
                                             date=current_date)
    except SignHoroscope.DoesNotExist:
        sign_hor = None

    if sign_hor:
        return render(request, 'zodiac/sign_horoscope.html', {'title': f'Гороскоп для {sign_slug}',
                                                              'current_date': current_date,
                                                              'sign': sign,
                                                              'sign_hor': sign_hor}, )
    else:
        url = 'https://ignio.com/r/export/utf/xml/daily/com.xml'
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'xml')
        txt = soup.find(f'{sign_slug}').find('today').text.strip()

        SignHoroscope.objects.create(sign_horoscope=txt,
                                     sign_id=sign,
                                     date=current_date)
        sign_hor = SignHoroscope.objects.get(sign_id__sign_name=f'{sign_slug}'.capitalize(),
                                             date=current_date)
        return render(request, 'zodiac/sign_horoscope.html', {'title': f'Гороскоп для {sign_slug}',
                                                              'current_date': current_date,
                                                              'sign': sign,
                                                              'sign_hor': sign_hor}, )


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')
