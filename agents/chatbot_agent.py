import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

def handle_chat():
    st.header("💬 Customer Support Chat")
    query = st.text_input("Ask your question")
    if query:
        llm = ChatOpenAI(
            openai_api_key="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",  # 🔐 TODO: Replace with your OpenRouter API key
            base_url="https://openrouter.ai/api/v1",
            model="mistralai/mistral-7b-instruct"
        )
        prompt = PromptTemplate(
            input_variables=["question"],
            template="""
            You are a helpful customer support agent.
            Answer the following question clearly:
            Question: {question}
            """
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(query)
        st.write("### Response:", response)
