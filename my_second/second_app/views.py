from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(a):
    return HttpResponse('<em>HELLO WORLD!!</em>')
