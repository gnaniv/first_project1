from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Anjali(request):
    return HttpResponse('Anjali,Gnani and Vani are 3 monkeys')

def Intelligent(request):
    return HttpResponse('<h1>Anjali is very intelligent girl</h1>')

def Vani(request):
    return HttpResponse('Vani is very innocent fellow')

def anjali(request):
    return HttpResponse('anjali is good girl')

