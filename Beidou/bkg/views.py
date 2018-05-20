from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import os
import json

# Create your views here.

def index(request):
    return render(request,'bkg/test.html')

def data(request):
    homedir = os.getcwd()
    fiel = open(homedir+'\\bkg\\static\\bkg\\data\\test.json','rb')
    data = json.load(fiel)
    
    return JsonResponse(data,safe=False) 

    