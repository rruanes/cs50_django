from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def ronnel(request):
    return HttpResponse('Hello, Ronnel!')

def ning(request):
    return HttpResponse('Hello, Ning!')

def greet(request, name):
    return render(request, 'hello/greet.html', {
        'name': name.capitalize()
    })