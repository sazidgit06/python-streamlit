import streamlit as st
st.title("Hello I am Sazid Hasan. Welcome to my web interface.")
st.subheader("Today we will learn about streamlit")
st.text("This is my first streamlit code. I am learning streamlit from Chai aur Code youtube channel.")
st.write("First task is to choose my favourite programming language using streamlit selectbox")

language = st.selectbox("Choose your favourite programming language: ", ["C", "C++", "JAVA", "Python", "JavaScript", "R", "C#", "PHP"])
st.write(f"You choose {language}.")
st.success("Excellent choise")