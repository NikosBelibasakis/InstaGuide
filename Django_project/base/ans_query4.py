import google.generativeai as genai
def ans_query(query, reviews, selected_language):
   
    try:
        genai.configure(api_key="MY_KEY")
        model = genai.GenerativeModel("gemini-1.5-flash")
        query = f"Using only the provided reviews: {reviews}, please address the following request or question related to the accommodation in {selected_language}. Please keep your response concise and under 300 words: {query}"
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None