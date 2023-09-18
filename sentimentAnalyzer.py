!pip install transformers
import streamlit as st
from transformers import pipeline

# Create the sentiment analysis pipeline using XLNet
classifier = pipeline("sentiment-analysis", model="xlnet-base-cased")
# Streamlit app title
st.title("Custom Sentiment Analysis")

# Text input for user to enter a tweet
user_input = st.text_area("Enter a tweet:")

# Function to analyze sentiment (replace with your custom model)
def analyze_sentiment(tweet):
    sentiment = classifier(tweet)[0]
    label = sentiment['label']
    score = sentiment['score']

    if label == 'LABEL_1':
        sentiment_text = "Positive"
    else:
        sentiment_text = "Negative"

    return f"Sentiment: {sentiment_text} (Score: {score:.2f})"

# Button to trigger sentiment analysis
if st.button("Analyze"):
    if user_input:
        # Call the sentiment analysis function
        sentiment = analyze_sentiment(user_input)
        st.write(f"Sentiment: {sentiment}")
