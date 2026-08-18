import streamlit as st
import pandas as pd


st.title("Welcome to streamlit basics")

file = st.file_uploader("Upload your file", type = ["CSV"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df)

if file:
    st.subheader("Data shape and data info")
    st.markdown(">Data shape")
    st.write(df.shape)
    st.markdown(">Duplicate data count")
    st.write(df.duplicated().sum())
    st.markdown(">Null values")
    st.write(df.isnull().sum())
    st.markdown(">Target column value counts")
    st.write(df['target'].value_counts())


