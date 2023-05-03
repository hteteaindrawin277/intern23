from django.shortcuts import render
from django.http import HttpResponse

def third(request):
    return HttpResponse("Hello  this is third web page")
def fourth(request):
    return render(request,'heading.html')

def members(request):
    return render(request,'firsthtml.html')

# Create your views here.

# Create your views here.
