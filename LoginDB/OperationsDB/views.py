from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import *

def startup(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        URL = 'http://127.0.0.1:5000/signup'
        param =  {
            'username' : request.POST['username'],
            'password' : request.POST['password'],
            'firstname': request.POST['firstname'],
            'age' : request.POST['age'],
        }
        try:
            response = requests.post(URL,json=param,timeout=300)
            data = response.text
        except:
            print('server busy') 
        return HttpResponse(data)
    else:
        return('Failed')


def login(request):
    if request.method == 'POST':       
        URL = 'http://127.0.0.1:5000/login'
        param =  {
            'username' : request.POST['username'],
            'password' : request.POST['password']
        } 
        try:
            response = requests.post(URL,json=param,timeout=300)
            data = response.text
            return HttpResponse(data)
        except:
            print('server busy') 
        return HttpResponse(data)
    else:
        return('Failed')
    


def fetch(request):
    data = getAllData()
    return HttpResponse(data)