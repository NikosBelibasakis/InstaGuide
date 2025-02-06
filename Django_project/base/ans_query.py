import openai

# Setting the OpenAI API key
openai.api_key = "MY_KEY"

def ans_query(query, reviews, selected_language):
    """
    Answer a query based on the accommodation reviews, responding in the selected language.
    """
    try:
        # Call to GPT-4o for generating an answer
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant that responds to requests and questions related to accommodation reviews. Always respond in {selected_language}."
                },
                {
                    "role": "user",
                    "content": f"Using only the provided reviews: {reviews}, please address the following request or question related to the accommodation. Please keep your response concise and under 300 words: {query}"
                }
            ],
           
        )
        
        # Get the answer
        answer = response['choices'][0]['message']['content']
        
        return answer

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
