import streamlit as st

st.title("This is class 2. We learning streamlit.")

if st.button("Order"):
    st.success("Your order is confirmed")

if st.checkbox("Add phone number"):
    phhone_number = st.text_input("Enter your phone number")
    st.write(f"Your phone number is {phhone_number}")

gender = st.radio("Select your gender", ["Male", "Female"])
st.write(f"Your gender is {gender}")

st.slider("Select your age", 18, 100)
st.number_input("How many children you have", min_value = 0, max_value = 10, step = 1)
name = st.text_input("Enter your name")
st.write(f"Welcome {name}")

date = st.date_input("Enter")
st.write(f"you entered {date}")