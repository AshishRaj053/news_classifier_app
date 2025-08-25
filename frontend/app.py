import streamlit as st
import requests

st.set_page_config(page_title="News Classifier", page_icon="📰", layout="centered")

st.title("📰 News Headline Classifier")

headline = st.text_area("Enter a news headline:")

if st.button("Classify"):
    if headline.strip() == "":
        st.warning("Please enter a headline.")
    else:
        try:
            # Send request to FastAPI backend
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"headline": headline}
            )

            if response.status_code == 200:
                result = response.json()
                st.success(f"**Predicted Category:** {result['category']}")
            else:
                st.error("⚠️ Error from backend. Check FastAPI logs.")

        except Exception as e:
            st.error(f"❌ Could not connect to backend: {e}")