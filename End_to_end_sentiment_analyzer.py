import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.write("# Suchit's Sentiment Analyzer")

user_input = st.text_input("Enter text to anlayze ->")
nltk.download("vader_lexicon")
s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

if score == 0:
    st.write(" ")
elif score["neg"] != 0:
    st.write("# Negative")
elif score["pos"] != 0:
    st.write("# Positive")
    
    #to run streamlit program... streamlit run filepath.py on anaconda prompt
