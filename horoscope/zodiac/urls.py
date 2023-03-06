from django.urls import path
from zodiac.views import *

urlpatterns = [
    path('', index, name='home'),
    path('<slug:sign_slug>', sign_horoscope, name='sign_horoscope'),

]
