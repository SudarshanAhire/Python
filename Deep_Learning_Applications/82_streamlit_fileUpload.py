import streamlit as st

st.title("Developed by Sudarshan Gokul Ahire")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF Uploaded Successfully")