import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"
        
        
    def get_response(self, user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response
        