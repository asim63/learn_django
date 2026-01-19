from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

monthly_challenges = {
    'january': 'Exercise daily for 30 minutes',
    'february': 'Read one book',
    'march': 'Learn something new each day',
    'april': 'Drink at least 2 liters of water daily',
    'may': 'Wake up early every day',
    'june': 'Practice a new skill for 20 minutes daily',
    'july': 'Avoid junk food for the entire month',
    'august': 'Write a daily journal entry',
    'september': 'Learn and revise one topic each day',
    'october': 'Limit social media usage to 30 minutes per day',
    'november': 'Express gratitude by writing one thankful note daily',
    'december': 'Reflect on the year and plan goals for next year',
}

def index(request):
    return HttpResponse("Welcome")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound("This month is not supported!")

def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]
    return HttpResponse(f"/testapp/{redirect_month}")