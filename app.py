import streamlit as st
from test4 import pipe
import pandas as pd
import time
import altair as alt

st.set_page_config(page_title="Sentiment Analysis")

st.title(":blue[Sentiment Analysis] Dashboard")

text = st.text_area("Enter text to be analyzed:")

if st.button("Analyze"):
    out = pipe(text)
    st.write(f"The sentiment of this statement is **{out[0]['label']}**.")

# allow csv uploads and analyze it

st.subheader("Analyze a file containing your reviews")
st.write("Only .csv files are allowed. It must contain only one column, named 'Reviews'.")
user_file = st.file_uploader("Upload your file:", type=['csv'])

if user_file:
    with st.spinner("Analyzing..."):
        time.sleep(2)

        data = pd.read_csv(user_file)
        data.columns = ["Reviews"]
        output = pipe([review for review in data['Reviews']])
        
        pos_count, neg_count = 0, 0
        for review in output:
            if review['label'] == "POSITIVE":
                pos_count += 1
            else:
                neg_count += 1
        
        st.markdown("### :green[Results]")
        st.write(f'Total number of reviews: {pos_count + neg_count}') 
        st.write(f'Positive reviews: {pos_count}')
        st.write(f'Negative reviews: {neg_count}')
        st.write(f'Positive percentage: {(pos_count / (pos_count + neg_count)) * 100}%')

        counts = pd.DataFrame([['Positive', pos_count], ['Negative', neg_count]])
        counts.columns = ['Sentiment', 'Count']
        chart = alt.Chart(counts).mark_bar().encode(
            x='Sentiment',
            y='Count'
        ).properties(
            width=300,
        )

        st.altair_chart(chart)