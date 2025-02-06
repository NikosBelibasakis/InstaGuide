import openai

# Setting the OpenAI API key
openai.api_key = "my_key"

def summarize_reviews(reviews, selected_language):
    """
    Summarizes the accommodation reviews and returns the summary in the selected language.
    """
    try:
        # Call to GPT-4o for generating a summary
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant that summarizes accommodation reviews. Always respond in {selected_language}."
                },
                {
                    "role": "user",
                    "content": f"Please provide a concise summary of the following accommodation reviews in a single paragraph, up to 200 words: {reviews}"
                }
            ],
            
        )
        
        # Get the summary
        summary = response['choices'][0]['message']['content']
        
        return summary

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
