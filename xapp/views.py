from django.shortcuts import render
from django.http import HttpResponse

def second(request):
    return HttpResponse("hello  this is sec page")
# Create your views here.
