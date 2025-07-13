import streamlit as st
import pandas as pd
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

FEEDBACK_FILE = os.path.abspath("feedback.csv")

def handle_feedback():
    st.header("📝 Leave Feedback")

    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        rating = st.slider("Rating", 1, 5)
        comments = st.text_area("Comments")
        submit = st.form_submit_button("Submit Feedback")

        if submit:
            # Get sentiment via OpenRouter (Mistral)
            llm = ChatOpenAI(
                openai_api_key="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",  # 🔐 Replace this
                base_url="https://openrouter.ai/api/v1",
                model="mistralai/mistral-7b-instruct"
            )
            prompt = PromptTemplate(
                input_variables=["feedback"],
                template="""
                Analyze sentiment of the following customer feedback and label it as Positive, Neutral, or Negative:
                Feedback: {feedback}
                Sentiment:
                """
            )
            chain = LLMChain(llm=llm, prompt=prompt)
            sentiment = chain.run(comments).strip()

            # Create new entry
            new_entry = {
                "Name": name,
                "Rating": rating,
                "Feedback": comments,
                "Sentiment": sentiment
            }

            # If file exists, load and append; else create
            if os.path.exists(FEEDBACK_FILE):
                df = pd.read_csv(FEEDBACK_FILE)
                df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            else:
                df = pd.DataFrame([new_entry])

            df.to_csv(FEEDBACK_FILE, index=False)
            st.success(f"Thank you! Feedback Sentiment: {sentiment}")
