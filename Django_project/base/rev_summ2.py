import openai

# Setting the OpenAI API key
openai.api_key = "my_key"

def summarize_reviews(reviews, selected_language):
   
    try:
        # Call to the o1-preview model for generating a summary
        response = openai.ChatCompletion.create(
            model="o1-preview",
            messages=[
               
                {
                    "role": "user",
                    "content": f"Please provide a concise summary of the following accommodation reviews in a single paragraph, up to 200 words, and write it in {selected_language}: {reviews}"
                }
            ],
            
        )
        
        # Get the summary
        summary = response['choices'][0]['message']['content']
        
        return summary

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
