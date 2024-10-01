from django.shortcuts import render
from apify_client import ApifyClient

def home(request):
    return render(request, 'home.html')

def get_reviews(request):
    if request.method == "POST":
        # Confirmation that the function is being triggered
        print("The get_reviews function is triggered.")

        # Retrieve the URL from the request
        url = request.POST.get('accommodationUrl')
        print(f"URL received: {url}")  # Display the URL in the console

        # API code for retrieving reviews
        client = ApifyClient("apify_api_62gCo1Y1AesGvCNQhIMye7ZJu9EGLA1zRBs6")
        run_input = {
            "url": url,
            "numberOfReviews": 15,
            "sortOrder": "Newest first",
        }

        run = client.actor("arel/booking-com-reviews-scraper").call(run_input=run_input)
        
        print('-'*50)
        print('Returned reviews: ')

        # Print the reviews
        counter = 1
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            title = item.get('title', 'No title available')
            positive_comment = item.get('positiveComment', 'No positive comment available')
            negative_comment = item.get('negativeComment', 'No negative comment available')

            print(f"Review {counter}:")
            print(f"Title: {title}")
            print(f"Positive Comment: {positive_comment}")
            print(f"Negative Comment: {negative_comment}")
            print('-' * 50)  # Separate reviews for readability

            counter += 1  # Increment the counter for the next review

    return render(request, 'home.html')  # Return the same page
