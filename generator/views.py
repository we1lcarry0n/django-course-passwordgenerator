from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator\home.html')

def password(request):


    chars = list('abcdefghijklmnopqrstuvwxyz')

    pslen = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))
    if request.GET.get('symbols'):
        chars.extend(list('!@#$%^&*()-_=+'))

    thepassword = ''

    for x in range(pslen):
        thepassword += random.choice(chars)


    return render(request, 'generator\password.html', {'password':thepassword})

def info(request):
    return render(request, 'generator\info.html')
