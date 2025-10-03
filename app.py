import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("data/sample_metadata_clean.csv")
   # the saved cleaned file from explore.py
    return df

data = load_data()

st.title("CORD-19 Research Papers Explorer")
st.write("A simple app to explore a cleaned sample of the CORD-19 dataset.")

st.subheader("Dataset Preview")
st.dataframe(data.head(20))


st.subheader("Search by Keyword")
keyword = st.text_input("Enter a keyword to search in abstracts:")

if keyword:
    results = data[data['abstract'].str.contains(keyword, case=False, na=False)]
    st.write(f"Found {len(results)} papers")
    st.dataframe(results[['title', 'abstract']].head(10))

st.subheader("Basic Stats")
st.write("Total Papers:", len(data))
st.write("Unique Authors:", data['authors'].nunique())


