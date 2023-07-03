import streamlit as st
import requests

if st.button('Call an API'):
    response = requests.get('https://api.example.com')
    st.write(response.json())