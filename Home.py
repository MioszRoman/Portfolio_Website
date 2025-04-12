import streamlit as st


content = """
Python, piercing & Poseidon 🐍💉⚡ |\n
Junior dev in progress | \n
Books and code make me happy 📚
"""

st.set_page_config(layout="wide")

st.title("My portfolio Website!")
st.subheader("Welcome to my personal portfolio website!")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=300)

with col2:
    st.info(content)

st.write("I will show you the projects:")