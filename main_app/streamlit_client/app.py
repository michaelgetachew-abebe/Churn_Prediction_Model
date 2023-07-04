import streamlit as st

def main_page():
    st.markdown("# SCHEDULED MODEL INFERENCE")
    st.sidebar.markdown("# Scheduled Model Inference")

def custom_infernce():
    st.markdown("# CUSTOM MODEL INFERENCE")
    st.sidebar.markdown("# Custom Model Inference")

def analytics():
    st.markdown("# ANALYTICS")
    st.sidebar.markdown("# Analytics")

page_names_to_funcs = {
    "SCHEDULED INFERENCE": main_page,
    "CUSTOM INFERENCE": custom_infernce,
    "ANALYTICS": analytics,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()