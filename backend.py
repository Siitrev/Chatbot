import openai, environ, os

env = environ.Env()
env.read_env(".env")
API_KEY = os.environ.get("API_KEY")


class Chatbot:
    def __init__(self):
        openai.api_key = API_KEY

    def get_response(self, user_input):
        response = (
            openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=4000,
                temperature=0.5,
            )
            .choices[0]
            .text
        )
        return response
