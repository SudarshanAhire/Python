import streamlit as st

st.title("Developed by Sudarshan Gokul Ahire")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}")