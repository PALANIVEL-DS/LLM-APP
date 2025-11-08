import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()  # ✅ loads .env file
api_key = os.getenv("GOOGLE_API_KEY")

st.title("🤖 Gemini Private Key Test")

if api_key:
    llm = GoogleGenerativeAI(
        model="models/gemini-2.5-flash-lite",
        google_api_key=api_key
    )
    response = llm.invoke("Say hello, I’m connected securely!")
    st.success("✅ Gemini Connected")
    st.write(response)
else:
    st.error("❌ No API key found in .env file")
