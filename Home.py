import streamlit as st
import pandas

content = """
Python, piercing & Poseidon 🐍💉⚡ |\n
Junior dev in progress | \n
Books and code make me happy 📚
"""

st.set_page_config(layout="wide")

df = pandas.read_csv("data.csv", sep=';')

st.title("My portfolio Website!")
st.subheader("Welcome to my personal portfolio website!")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=300)

with col2:
    st.info(content)

st.write("I will show you the projects:")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")
