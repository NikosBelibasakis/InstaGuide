import openai

# Setting the OpenAI API key


def summarize_reviews(reviews):
    
    #We receive the combined text of the reviews and return their summary using GPT-4o-mini.
    
    try:
        # Call to GPT-4o-mini for generating a summary
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes hotel reviews."},
                {"role": "user", "content": f"Please summarize the following hotel reviews in a single paragraph, and make sure the summary is no longer than 150 words: {reviews}"}
            ],
            max_tokens= 250,  # Set the maximum number of tokens (words/characters) for the model's response (the summary)
        )
        
        # Get the summary
        summary = response['choices'][0]['message']['content']
                        
        return summary

    except Exception as e:
        print(f"An error occurred: {e}")
        return None