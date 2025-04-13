# AI Study Buddy

This project is a simple terminal-based AI chatbot designed to act as a supportive study companion. It uses OpenAI's GPT-4o-mini model to respond to user inputs and provide guidance, motivation, or academic assistance in real time.

## Features

- Chat interface that runs in the terminal
- Integrates with OpenAI API (GPT-4o-mini)
- Dynamically responds to user messages
- Recognizes exit commands to gracefully end the session

## Project Files

### `ai_study_buddy.py`

A Python script that:

- Loads OpenAI credentials from environment variables:
  - `OPENAI_API_KEY`
  - `OPENAI_PROJECT` (optional)
  - `OPENAI_ORG` (used by the OpenAI client)
- Initializes the OpenAI client
- Defines a `get_response()` function that sends a prompt to the GPT-4o-mini model
- Runs a `main()` loop to continuously accept user input and return responses

## Environment Variables

To run this script, you must define the following environment variables in your shell or `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key  
- `OPENAI_ORG`: Your OpenAI organization ID  
- `OPENAI_PROJECT`: (Optional) Your OpenAI project ID  

Example (Unix/macOS):

```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxx"
export OPENAI_ORG="org-xxxxxxxxxxxx"
export OPENAI_PROJECT="proj-xxxxxxxxxxxx"
```

## How to Run

Make sure you have the `openai` Python package installed:

```bash
pip install openai
```

Then, run the chatbot:

```bash
python ai_study_buddy.py
```

Type your question, problem, or feeling. Type `exit` or `quit` to end the session.

## Example Interaction

```
Hi! I'm your AI Study Buddy. Type how you're feeling or what you're struggling with.
(Type 'exit' to quit.)

You: I'm feeling overwhelmed with my workload.

AI Study Buddy: It’s okay to feel overwhelmed sometimes. Let's break your tasks into smaller steps. What’s your most urgent priority right now?
```

## Technologies Used

- Python 3.x  
- OpenAI API (`openai` package)  
- Terminal-based input/output

## Future Plans

- Add support for saving conversations  
- Build a web version using Streamlit or Flask  
- Integrate study resource recommendations based on input  
- Add sentiment analysis to detect emotional states

