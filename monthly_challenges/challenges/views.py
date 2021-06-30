from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month-1]
    # return HttpResponse(f"This is a month represented by the number {month}")
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # return HttpResponseRedirect(f"/challenges/{redirect_month}/")
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
