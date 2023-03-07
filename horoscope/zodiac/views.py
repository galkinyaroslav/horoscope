from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from zodiac.models import ZodiacSign, SignHoroscope
from datetime import date
from bs4 import BeautifulSoup
import requests

# Create your views here.
current_date = date.today()


# zodiac_sign_pic_list = ['&#9800',
#                         '&#9801',
#                         '&#9802',
#                         '&#9803',
#                         '&#9804',
#                         '&#9805',
#                         '&#9806',
#                         '&#9807',
#                         '&#9808',
#                         '&#9809',
#                         '&#9810',
#                         '&#9811', ]


def index(request):
    zodiac_signs = ZodiacSign.objects.all()
    return render(request, 'zodiac/index.html', {'title': 'Главная страница',
                                                 'current_date': current_date,
                                                 # 'pics': zodiac_sign_pic_list,
                                                 'zodiac_signs': zodiac_signs}, )


def sign_horoscope(request, sign_slug):
    # if sign not in ZodiacSigns.object.all(): ToDo
    #     return redirect('home')

    sign = ZodiacSign.objects.get(sign_name=f'{sign_slug}'.capitalize())
    try:
        sign_hor = SignHoroscope.objects.get(sign_id__sign_name=f'{sign_slug}'.capitalize(),
                                             date=current_date)
    except SignHoroscope.DoesNotExist:
        sign_hor = None

    if sign_hor:
        return render(request, 'zodiac/sign_horoscope.html', {'title': f'Гороскоп для {sign_slug}',
                                                              'current_date': current_date,
                                                              # 'pics': zodiac_sign_pic_list,
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
    # return HttpResponse(f'<h1>TEST SLUG</h1><p>{sign_slug}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')
