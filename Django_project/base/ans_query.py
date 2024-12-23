import openai

# Setting the OpenAI API key
openai.api_key = "MY_KEY"

def ans_query(query, reviews, selected_language):
    """
    Answer a query based on the accommodation reviews, responding in the selected language.
    """
    try:
        # Call to GPT-4o-mini for generating an answer
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant that responds to requests and questions related to accommodation reviews. Always respond in {selected_language}."
                },
                {
                    "role": "user",
                    "content": f"Based on these reviews only: {reviews}, please respond to the following request or question regarding the accommodation in less than 200 words: {query}"
                }
            ],
            max_tokens=500,  # Set the maximum number of tokens (words/characters) for the model's answer
        )
        
        # Get the answer
        answer = response['choices'][0]['message']['content']
        
        return answer

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
