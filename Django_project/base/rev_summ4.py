import google.generativeai as genai

def summarize_reviews(reviews, selected_language):
   
    try:
        genai.configure(api_key="my_key")
        model = genai.GenerativeModel("gemini-1.5-flash")
        query = f"Please provide a concise summary of the following accommodation reviews in a single paragraph, up to 200 words, and write it in {selected_language}: {reviews}"
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None