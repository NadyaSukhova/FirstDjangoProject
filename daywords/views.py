from django.shortcuts import render
from django.http import HttpResponse
import random

def index (request):
    lines = open('C:\\Users/Hope/PycharmProjects/FirstTry/words.txt').read().splitlines()
    myline = {"word": random.choice(lines)}
    return render(request, 'mainApp/dayword.html', context=myline)

# Create your views here.