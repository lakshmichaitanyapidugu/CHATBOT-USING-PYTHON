import openai
openai.api_key = "your api-key here"

def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("Bot:", chat(user_input))