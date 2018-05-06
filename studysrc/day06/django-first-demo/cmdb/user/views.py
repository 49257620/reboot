#encoding: utf-8
from django.shortcuts import render

from django.http import HttpResponse
from user import user
import time 

def index(request):
    users = user.load_data()
    # return HttpResponse('My First Page!')
    return render(request,'user/index.html',{
        'current_time':time.asctime(time.localtime(time.time())),
        'users':users.items()
    })

# Create your views here.
