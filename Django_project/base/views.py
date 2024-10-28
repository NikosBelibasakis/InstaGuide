from django.http import HttpResponse
from django.shortcuts import render
from base.get_rev import get_rev
from base.rev_summ import summarize_reviews
from base.ans_query import ans_query

reviews = None


def home(request):
    return render(request, 'home.html')

def get_reviews(request):
    global reviews
    if request.method == "POST":
        url = request.POST.get('accommodationUrl')
        reviews = get_rev(url)
        return HttpResponse(0)
        

def cr_summ(request):
    global reviews
    if request.method == "POST":
        reviews_summary = summarize_reviews(reviews)
        return HttpResponse(reviews_summary)


def get_query(request):
    global reviews
    if request.method == "POST":
        query = request.POST.get('specificInfo')
        
        if reviews is None:
            
            return HttpResponse("no_url")
                
        answer = ans_query(query, reviews)
        return HttpResponse(answer)
    

def clear_reviews(request):
    global reviews
    reviews = None
    return HttpResponse("Reviews cleared.")
