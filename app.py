import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI  

api_key = st.secrets.get("GOOGLE_API_KEY")

st.set_page_config(page_title="🤖 Gemini Secure LLM", page_icon="🤖", layout="centered")
st.title("🤖 Gemini 2.5 Flash Lite — Secure Streamlit App")

if api_key:
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            temperature=0.2,
            max_output_tokens=512,
            google_api_key=api_key
        )
        response = llm.invoke("Say hello, I’m connected securely on Streamlit Cloud!")
        st.success("✅ Gemini Connected Successfully!")
        st.write("**Model Response:**", response.content if hasattr(response, 'content') else response)

    except Exception as e:
        st.error(f"⚠️ Gemini Initialization Failed: {e}")
else:
    st.error("❌ No API key found. Add it in Streamlit → Settings → Secrets → GOOGLE_API_KEY")
