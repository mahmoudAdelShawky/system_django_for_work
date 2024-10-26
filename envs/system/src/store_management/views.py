from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render (request , '../templates/index.html')

def store_management(request):
    return render (request , '../templates/tables.html')

