import openai

# Setting the OpenAI API key
openai.api_key = "MY_KEY"

def summarize_reviews(reviews, selected_language):
    """
    Summarizes the accommodation reviews and returns the summary in the selected language.
    """
    try:
        # Call to GPT-4o-mini for generating a summary
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant that summarizes accommodation reviews. Always respond in {selected_language}."
                },
                {
                    "role": "user",
                    "content": f"Please summarize the following accommodation reviews in a single paragraph, and make sure the summary is no longer than 200 words: {reviews}"
                }
            ],
            max_tokens=500,  # Set the maximum number of tokens for the model's response
        )
        
        # Get the summary
        summary = response['choices'][0]['message']['content']
        
        return summary

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
