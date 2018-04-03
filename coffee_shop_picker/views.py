from django.http import HttpResponse
from django.shortcuts import render
from . import decision_tree as dt
import scipy

def index(request):
    return render(request, 'index.html')

def pickr(request):
    budget = float(request.POST['budget'])
    if 'hasWifi' in request.POST:
        wifi = float(request.POST['hasWifi'])
    else:
        wifi = 0.0
    environment = float(request.POST['environment'])
    quality = float(request.POST['quality'])
    noise = float(request.POST['noise'])
    prediction = dt.predict(budget, wifi, environment, quality, noise)
    #predict = string(prediction[0])
    predict = str(prediction[0])
    print(predict == 'kivhan')
    if(predict == 'kivhan'):
        return kivhan(request)
    elif(predict == 'seattles'):
        return seattles(request)
    elif(predict == 'bos'):
        return bos(request)
    elif(predict == 'gloriajeans'):
        return gloriajeans(request)


def kivhan(request):
    return render(request, 'kivhan.html')

def seattles(request):
    return render(request, 'seattles.html')

def bos(request):
    return render(request, 'bos.html')

def gloriajeans(request):
    return render(request, 'gloriajeans.html')
