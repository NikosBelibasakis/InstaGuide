from apify_client import ApifyClient
from concurrent.futures import ThreadPoolExecutor, as_completed


# Uses the 'Booking.com Reviews Scraper' by Apify to get the reviews of the given accommodation
def get_rev(url):
    client = ApifyClient("apify_api_VHvKCWnWG63SxqA87sBZV31NKoHtfP0u9jjc")
    run_input = {
        "url": url,
        "numberOfReviews": 20,
        "sortOrder": "Newest first",
    }

    run = client.actor("arel/booking-com-reviews-scraper").call(run_input=run_input)
    reviews = client.dataset(run["defaultDatasetId"]).iterate_items()

    # Processes a review.
    def process_review(rev):
        title = rev.get('title', 'No title available')
        positive_comment = rev.get('positiveComment', 'No positive comment available')
        negative_comment = rev.get('negativeComment', 'No negative comment available')

        # Concatenate all parts of the review into one text and translate once if needed
        combined_text = f"{title}. {positive_comment}. {negative_comment}."
        return combined_text + "\n"

    # We use a thread pool to process reviews in parallel
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(process_review, review): review for review in reviews}

        # Collect the reviews in a list
        total_reviews = []
        for future in as_completed(futures):
            total_reviews.append(future.result())
    
    # Convert the list of reviews into a single string
    combined_reviews = " ".join(total_reviews)
       
    # Return the reviews
    return combined_reviews
