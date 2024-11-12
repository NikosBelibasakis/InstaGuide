from apify_client import ApifyClient
from concurrent.futures import ThreadPoolExecutor, as_completed

# Uses the 'Booking.com Reviews Scraper' by Apify to get the reviews of the given accommodation
def get_rev2(url):
    client = ApifyClient("apify_api_VHvKCWnWG63SxqA87sBZV31NKoHtfP0u9jjc")
    run_input = {
        "reviewUrls": [{"url": url}],
        "maxResults": 200,
        "sorter": "MOST_RELEVANT",
    }

    run = client.actor("ha1poFT8aWXtFvnaQ").call(run_input=run_input)
    reviews = client.dataset(run["defaultDatasetId"]).iterate_items()

    # Processes a review with the new structure.
    def process_review(rev):
        title = rev.get('title', 'No title available')
        positive_comment = rev.get('positiveText', 'No positive comment available')
        negative_comment = rev.get('negativeText', 'No negative comment available')
        review_date = rev.get('reviewedDate', 'No review date available')
        reviewer_country = rev.get('countryName', 'No country name available')

        # Formatted review structure
        formatted_review = (
            "Review:\n"
            f"- Reviewer Country: {reviewer_country}\n"
            f"- Review Date: {review_date}\n"
            f"- Title: {title}\n"
            f"- Positive Comment: {positive_comment}\n"
            f"- Negative Comment: {negative_comment}\n"
            "---\n"
        )
        return formatted_review

    # We use a thread pool to process reviews in parallel
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(process_review, review): review for review in reviews}

        # Collect the reviews in a list
        total_reviews = []
        for future in as_completed(futures):
            total_reviews.append(future.result())

    # Convert the list of reviews into a single string with clear separation
    combined_reviews = " ".join(total_reviews)
    
    # Return the reviews
    return combined_reviews