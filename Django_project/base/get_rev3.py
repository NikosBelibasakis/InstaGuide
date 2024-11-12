import asyncio
import httpx
from parsel import Selector
from urllib.parse import urlparse

# Function to extract the cc1 and pagename parameters from the URL
def extract_params_from_url(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    cc1 = path_parts[2]
    pagename = path_parts[3].split('.')[0]
    
    return cc1, pagename


# Async function to fetch a single review's data
async def get_review_data(review):
    review_date = review.css(".c-review-block__date::text").get(default="N/A").strip()
    review_title = review.css(".c-review-block__title::text").get(default="N/A").strip()
    reviewer_country = review.css(".bui-avatar-block__subtitle::text").get(default="N/A").strip()   
    
    # Get all the reservation details and extract the traveller type
    res_details = review.css(".bui-list__body::text").getall()
    traveller_type = res_details[3].strip() if len(res_details) > 3 else "N/A"

    # Get all text parts and label them as positive and negative
    review_text_parts = review.css('.c-review__body ::text').getall()
    positive_text = review_text_parts[0].strip() if len(review_text_parts) > 0 else "N/A"
    negative_text = review_text_parts[1].strip() if len(review_text_parts) > 1 else "N/A"
    
    return (
        "Review:\n"
        f"Date: {review_date}\n"
        f"Reviewer counrty: {reviewer_country}\n"
        f"Traveller type: {traveller_type}\n"
        f"Title: {review_title}\n"
        f"Positive text: {positive_text}\n"
        f"Negative text: {negative_text}\n"
        "---\n"
    )


# Async function to fetch reviews with specific offset
async def fetch_reviews(offset, base_url, params, headers):
    params["offset"] = offset
    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        selector = Selector(response.text)
        reviews = selector.css(".review_list_new_item_block")
        
        # If no reviews are found, return None
        if not reviews:
            return None
        
        # Run get_review_data concurrently for all reviews in this page
        review_data = await asyncio.gather(*(get_review_data(review) for review in reviews))
        return review_data

# Main async function to run the tasks
async def get_rev3(url):
    
    cc1, pagename = extract_params_from_url(url)

    # Settings for retrieving reviews
    base_url = "https://www.booking.com/reviewlist.en-gb.html"
    params = {
        "cc1": cc1,
        "pagename": pagename,
        "rows": 25
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    # List of offsets (to fetch 200 reviews maximum)
    offsets = [0, 25, 50, 75, 100, 125, 150, 175]

    # Run parallel async requests
    total_reviews = []
    tasks = [fetch_reviews(offset, base_url, params, headers) for offset in offsets]
    results = await asyncio.gather(*tasks)

    for result in results:
        if result:
            total_reviews.extend(result)

    # Convert the list of reviews into a single string
    combined_reviews = " ".join(total_reviews)
    
    return combined_reviews


