from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "challenge for january",
    "february": "challenge for february",
    "march": "challenge for march",
    "april": "challenge for april",
    "may": "challenge for may",
    "june": "challenge for june",
    "july": "challenge for july",
    "august": "challenge for august",
    "september": "challenge for september",
    "october": "challenge for october",
    "november": "challenge for november",
    "december": "challenge for december"
}


# Create your views here.
def index(request):
    return HttpResponse("Index of the Challenges App!")

# def january(request):
#     return HttpResponse("Challenge for January")

# def february(request):
#     return HttpResponse("Challenge for February")


def monthly_challenge_by_number(request, month):
    return HttpResponse(f"This is a month represented by the number {month}")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)
