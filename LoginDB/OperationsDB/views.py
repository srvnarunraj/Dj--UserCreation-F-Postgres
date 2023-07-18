from django.shortcuts import render

def startup(request):
    return render(request,'index.html')
