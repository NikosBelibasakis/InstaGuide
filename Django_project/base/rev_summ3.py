import anthropic

# Setting the Anthropic API key
client = anthropic.Anthropic(
    
    api_key="my_key"
)


def summarize_reviews(reviews, selected_language):
   
    try:
        # Call to the claude 3.5 sonnet for generating a summary
        message = client.messages.create(
    model="claude-3-5-sonnet-latest",
    max_tokens=1024,
    messages=[
        {"role": "user", 
         "content": f"Please provide a concise summary of the following accommodation reviews in a single paragraph, up to 200 words, and write it in {selected_language}: {reviews}"}
        ]
       )
        
        # Get the summary
        summary = message.content[0].text
        return summary

    except Exception as e:
        print(f"An error occurred: {e}")
        return None







