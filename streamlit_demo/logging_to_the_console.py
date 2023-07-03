import streamlit as st

st.write("Hello, world!")
st.write("This is a Streamlit app.")

# Log a message to the browser console
st.write("Logging a message to the console...")
js = "console.log('Hello from Streamlit!')"
html = f"<script>{js}</script>"
st.write(html, unsafe_allow_html=True)
