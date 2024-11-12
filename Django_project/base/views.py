from django.http import HttpResponse
from django.shortcuts import render
from base.get_rev3 import get_rev3
from base.rev_summ import summarize_reviews
from base.ans_query import ans_query
import asyncio

reviews = None
selected_language = None

def home(request):
    return render(request, 'home.html')

def get_reviews(request):
    global reviews
    global selected_language
    if request.method == "POST":
        url = request.POST.get('accommodationUrl')
        selected_language = request.POST.get('language')
        reviews = asyncio.run(get_rev3(url))
        return HttpResponse(0)
        

def cr_summ(request):
    global reviews
    if request.method == "POST":
        reviews_summary = summarize_reviews(reviews,selected_language)
        return HttpResponse(reviews_summary)


def get_query(request):
    global reviews
    global selected_language
    if request.method == "POST":
        query = request.POST.get('specificInfo')
        selected_language = request.POST.get('language')
        
        if reviews is None:
            
            return HttpResponse("no_url")
                
        answer = ans_query(query, reviews, selected_language)
        return HttpResponse(answer)
    

def clear_reviews(request):
    global reviews
    reviews = None
    return HttpResponse("Reviews cleared.")
