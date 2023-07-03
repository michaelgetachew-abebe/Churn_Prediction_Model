import streamlit as st
import requests

def fetch(session, url):
    try:
        result = session.get(url)
        return result
    except Exception:
        return {}