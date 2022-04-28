from django.http import HttpResponse
from django.shortcuts import render

def skills(request):
    return HttpResponse('<h1>Ca marche</h1>')

def experiences(request):
    return HttpResponse('<h2>Exp</h2>')

def cursus(request):
    return HttpResponse('<h2>cursus</h2>')