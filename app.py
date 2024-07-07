import streamlit as st
from test4 import pipe

st.set_page_config(page_title="Sentiment Analysis")

st.title("Sentiment Analysis (Testing Phase)")

text = st.text_area("Enter text to be analyzed:")

if st.button("Analyze"):
    out = pipe(text)
    st.write(f"The sentiment of this statement is **{out[0]['label']}**.")