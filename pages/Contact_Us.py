import streamlit as st

st.set_page_config(layout="wide")
st.title("Contact Us")

with st.form(key="email_forms"):
    user = st.text_input("Give us your email: ")
    message = st.text_area("Write your message:")
    button = st.form_submit_button("Submit")