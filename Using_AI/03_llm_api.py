import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key=os.getenv("API_KEY")

client = OpenAI(api_key)

completion = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?",
        },
    ],
)

print(completion.choices[0].message.content)









from openai import OpenAI
client=OpenAI(api_key="keys.txt")

response=client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {
            "role":"user",
            "content": 7-23
        }
    ],
    response_format={
        "type":"text"
    },
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
for choices in response.choices:
    print(choices.message.content)