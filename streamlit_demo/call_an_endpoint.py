import streamlit as st
import requests
import config

if st.button('Call an API'):
    name = 'Lufthansa'
    api_url = 'https://api.api-ninjas.com/v1/airlines?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': config.api_key})
    st.write(response.json())