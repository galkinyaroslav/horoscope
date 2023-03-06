from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:sign>', views.zodiac_sign, name='zodiac_sign'),

]
