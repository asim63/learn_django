from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse
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
    # list_items = ""
    # months = list(monthly_challenges.keys())
    # for month in months:
    #     capitalMonth = month.capitalize()
    #     redirect_url = reverse('monthly-challenge',args=[month.lower()])
    #     list_items += f"<li><a href='{redirect_url}'>{capitalMonth}</a></li>"
    # return HttpResponse(f"<ul>{list_items}</ul>")
    
    months = list(monthly_challenges.keys())

    return render(request, "testapp/index.html", {
        "months": months
    })
    # html="""
    #     <ul>
    #         <li><a href="/testapp/january/">January</a></li>
    #         <li><a href="/testapp/february/">February</a></li>
    #     </ul>
    # """

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
       # return HttpResponse(f"<h1>{month} challenge: {challenge_text}</h1>")
        return render(request,'testapp/challenge.html', {
            "text": challenge_text,
            "month_name" : month.capitalize()
        })
    except KeyError:
        return HttpResponseNotFound("<h1>This is not available</h1>")

def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]
    redirect_url = reverse("monthly-challenge", args=[redirect_month])
    return redirect(redirect_url)