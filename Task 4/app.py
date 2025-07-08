# app.py
import streamlit as st
import joblib

# Load model & vectorizer
model = joblib.load("model/spam_classifier_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# Title
st.title("📩 SMS Spam Classifier")

st.write("Enter an SMS message below and click Predict to see if it's Spam or Not Spam.")

# Text input
sms_input = st.text_area("📨 Type your SMS here:")

# Predict button
if st.button("🔍 Predict"):
    if sms_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        vectorized_input = vectorizer.transform([sms_input])
        prediction = model.predict(vectorized_input)[0]

        if prediction == 1:
            st.error("🚫 This message is **SPAM**.")
        else:
            st.success("✅ This message is **NOT SPAM**.")
