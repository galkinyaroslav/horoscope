from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader


# Create your views here.

def home(request):
    return render(request, 'home.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')
