import time

import streamlit as st
from google import genai
from google.genai import types


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝"
)


# -----------------------------
# App title
# -----------------------------

st.title("📝 AI Text Summarizer")
st.write("Paste your text and let AI create a concise summary.")


# -----------------------------
# Gemini client
# -----------------------------

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


# -----------------------------
# User input
# -----------------------------

text = st.text_area(
    "Paste your text",
    height=300,
    placeholder="Paste an article, notes, or any long text here..."
)


# -----------------------------
# Summary length
# -----------------------------

summary_length = st.selectbox(
    "Choose summary length",
    ["Short", "Medium", "Detailed"]
)


# -----------------------------
# Summarize
# -----------------------------

if st.button("Summarize"):

    if not text.strip():

        st.warning("Please enter some text first.")

    else:

        with st.spinner("Generating summary..."):

            response = None

            for attempt in range(3):

                try:

                    response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",

                        contents=f"""
Summarize the following text.

Summary length: {summary_length}

Text:
{text}
""",

                        config=types.GenerateContentConfig(
                            system_instruction="""
You are an AI text summarizer.

Your job is to:
- Create clear and useful summaries.
- Keep the most important information.
- Remove unnecessary details.
- Use simple and easy-to-understand language.
- Follow the requested summary length.
"""
                        )
                    )

                    break

                except Exception as e:

                    if "503" in str(e) and attempt < 2:
                        time.sleep(3 * (attempt + 1))

                    else:
                        st.error(
                            "Gemini is temporarily unavailable. "
                            "Please try again later."
                        )
                        st.stop()


        # -----------------------------
        # Display results
        # -----------------------------

        if response:

            st.subheader("Result")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 📄 Original Text")
                st.write(text)

            with col2:
                st.markdown("### ✨ AI Summary")
                st.write(response.text)

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.markdown(
    """
    <div style='text-align: center;'>
        Created by <b>Sanjay</b> ❤️<br>
        sanch.builds@gmail.com
    </div>
    """,
    unsafe_allow_html=True
)