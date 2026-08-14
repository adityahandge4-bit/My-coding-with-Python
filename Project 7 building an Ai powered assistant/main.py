
 # API key used to authenticate requests to OpenAI
import os  # import operating system utilities (not used in current code)
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI  # import the OpenAI client class from the openai package

# Conversation history list for chat completion context
messages = []  # store user and assistant messages for the chat session

# Initialize OpenAI client with API key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("API-KEY")
)

# Send a user message to the model and print the assistant response
def completion(message):
    global messages  # refer to the global messages list defined above

    # Add the user prompt to the conversation history
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    # Create a chat completion request using the full message history
    chat_completion = client.chat.completions.create(messages=messages, model="gpt-4o")

    # Build the assistant response object from API output
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }

    # Add assistant response to history for future context
    messages.append(message)

    # Display the assistant response in the console
    print(f"Jarvis:{message['content']}")

if __name__ == "__main__":
    # Start the assistant and read user input in a loop
    print("Jarvis:Hi I am Jarvis,How may I help you ?\n")
    while True:
        user_question = input()  # read a line of input from the user
        print(f"User:{user_question}")  # print the user's message to the console
        completion(user_question)  # send the user's question to the completion function
