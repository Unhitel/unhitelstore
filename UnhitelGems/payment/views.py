from django.shortcuts import render
from django.http import HttpResponse

def success(request):
    return HttpResponse("<h1>Оплата прошла успешно</h1>")

def rejected(request):
    return HttpResponse("<h1>Оплата не прошла</h1>")
