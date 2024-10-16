from django.http import HttpResponse
from django.shortcuts import render
from base.get_rev import get_rev
from base.rev_summ import summarize_reviews

def home(request):
    return render(request, 'home.html')

def get_reviews(request):
    if request.method == "POST":
        print("The get_reviews function has been triggered.")
        url = request.POST.get('accommodationUrl')
        print(f"Received URL: {url}")

        
        reviews = get_rev(url)

        
        reviews_summary = summarize_reviews(reviews)

        
        return HttpResponse(reviews_summary)
