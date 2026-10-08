
import streamlit as st

st.title("Simple Form")

with st.form("my_form"):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")

    submit = st.form_submit_button("Submit")

if submit:
    st.write("Name:", name)
    st.write("Email:", email)
    st.success("Form submitted successfully!")