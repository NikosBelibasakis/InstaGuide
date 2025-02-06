import openai

# Setting the OpenAI API key
openai.api_key = "MY_KEY"

def ans_query(query, reviews, selected_language):
    """
    Answer a query based on the accommodation reviews, responding in the selected language.
    """
    try:
        # Call to the o1-preview model for generating an answer
        response = openai.ChatCompletion.create(
            model="o1-preview",
            messages=[
               
                {
                    "role": "user",
                    "content": f"Using only the provided reviews: {reviews}, please address the following request or question related to the accommodation in {selected_language}. Please keep your response concise and under 300 words: {query}"
                }
            ],
            
        )
        
        # Get the answer
        answer = response['choices'][0]['message']['content']
        
        return answer

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
