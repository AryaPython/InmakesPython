from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def forest(request):
    return HttpResponse("Welcome to my new home")