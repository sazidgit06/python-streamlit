import streamlit as st

st.title("Welcome to our cafe")

col1, col2 = st.columns(2)

with col1:
    st.header("Adrak chai")
    st.image("https://images.pexels.com/photos/28617425/pexels-photo-28617425.jpeg", width = 200)
    vote_adrak = st.button("Vote adrak chai")

with col2:
    st.header("Masala chai")
    st.image("https://images.pexels.com/photos/17286803/pexels-photo-17286803.jpeg", width = 200)
    vote_masala = st.button("vote masala chai")

if vote_adrak:
    st.success("Thanks for voting adrak chai")

else:
    st.success("Thanks for voting masala chai")

name = st.sidebar.text_input("Enter your name")
st.sidebar.write(f"Welcome {name}")