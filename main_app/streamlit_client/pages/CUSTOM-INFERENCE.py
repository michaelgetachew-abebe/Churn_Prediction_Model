import streamlit as st
import pandas as pd
import requests


def main():
    st.markdown("<h1 style= 'color: green;'>Custom Model Inference</h1>", unsafe_allow_html=True)
    dataset_file = st.file_uploader("Upload a Custom Dataset(.csv)", type=["csv"])
    url = "https://file.io/"
    if dataset_file is not None:
        df = pd.read_csv(dataset_file)
        st.dataframe(df)
        df.to_csv('custom.csv')
        submit = st.button("Run Model Inference")
        if submit:
            with open("./custom.csv", 'rb') as f:
                response = requests.post(url, files={'file': f})

    
if __name__ == "__main__":
    main()