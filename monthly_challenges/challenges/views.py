from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse("Index of the Challenges App!")

# def january(request):
#     return HttpResponse("Challenge for January")

# def february(request):
#     return HttpResponse("Challenge for February")

def monthly_challenge(request, month):
    if month == "january" or month == "february" or month == "march":
        return HttpResponse(f"Challenge for {month}")
    else:
        return HttpResponseNotFound("This month is not supported")