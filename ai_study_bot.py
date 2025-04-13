
import os
print(os.environ.get('OPENAI_API_KEY')) 


_open_ai_tkn = os.environ.get('OPENAI_API_KEY')
_project_tkn = os.environ.get('OPENAI_PROJECT')
_organisation_tkn = os.environ.get('OPENAI_ORG')
print(_open_ai_tkn)

import openai
import os
from openai import OpenAI

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG")
)

def get_response(prompt):
    response = client.chat.completions.create(
    model="gpt-4o-mini", 
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)
    return response.choices[0].message.content


def main():
    print("Hi! I'm your AI Study Buddy. Type how you're feeling or what you're struggling with.\n(Type 'exit' to quit.)\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("AI Study Buddy: You've got this!! Take care!")
            break

        reply = get_response(user_input)
        print(f"\nAI Study Buddy: {reply}\n")

if __name__ == "__main__":
    main()