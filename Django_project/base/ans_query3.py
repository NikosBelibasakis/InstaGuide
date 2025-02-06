import anthropic

# Setting the Anthropic API key
client = anthropic.Anthropic(
    
    api_key="MY_KEY"
)


def ans_query(query, reviews, selected_language):
   
    try:
        # Call to the claude 3.5 sonnet for generating an answer
        message = client.messages.create(
    model="claude-3-5-sonnet-latest",
    max_tokens=1024,
    messages=[
        {"role": "user", 
         "content": f"Using only the provided reviews: {reviews}, please address the following request or question related to the accommodation in {selected_language}. Please keep your response concise and under 300 words: {query}"}
        ]
       )
        
        # Get the answer
        answer = message.content[0].text
        return answer

    except Exception as e:
        print(f"An error occurred: {e}")
        return None







