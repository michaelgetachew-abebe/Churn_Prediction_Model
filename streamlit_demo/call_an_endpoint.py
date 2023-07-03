import streamlit as st
# import requests
import httpx
import config

if st.button('Call an API'):
    api_url = "https://api.api-ninjas.com/v1/dadjokes?limit="
    response = httpx.get("https://api.api-ninjas.com/v1/dadjokes?limit=2", headers={'X-Api-Key': config.api_key},verify=False)
    st.write(response.json())