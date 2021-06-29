from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index of the Challenges App!")

def january(request):
    return HttpResponse("Challenge for January")

def february(request):
    return HttpResponse("Challenge for February")
