# AI Text Summarizer

A simple text summarizer built with Python, Streamlit, and the Google Gemini API.

## What it does

- Takes text as input
- Generates a summary using Gemini
- Supports three summary lengths:
  - Short
  - Medium
  - Detailed
- Displays the original text and generated summary

## Tech Used

- Python
- Streamlit
- Google Gemini API
- `google-genai`

## How it works

The application sends the user's text to Gemini along with instructions for how the summary should be generated.

```text
Text Input
    ↓
Summary Length
    ↓
Prompt + Context
    ↓
Gemini API
    ↓
Generated Summary
```

## Project Structure

```text
ai-text-summarizer/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

The Gemini API key is stored locally in Streamlit secrets and is not included in the repository.

## Run Locally

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd ai-text-summarizer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create:

```text
.streamlit/secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

Run the application:

```bash
streamlit run app.py
```

## What I Learned

- System prompts
- User prompts
- Context
- Tokens
- Calling an LLM API from Python
- Basic prompt design
- Handling API errors
- Using Streamlit to build a simple interface
- Keeping API keys out of GitHub

## Future Improvements

- PDF and document upload
- Download summary
- Copy summary button
- Better UI
- Token usage display
- Online deployment

## Author

**Sanjay**

B.Tech Artificial Intelligence & Machine Learning

sanch.builds@gmail.com
