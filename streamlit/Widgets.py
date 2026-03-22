import streamlit as st

st.title("Strimlet text input")

name=st.text_input("Enter your name")
if name:
    st.write(f"Hello {name}")
