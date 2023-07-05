import streamlit as st
import pandas as pd

def main():
    st.markdown("<h1 style= 'color: green;'>Custom Model Inference</h1>", unsafe_allow_html=True)
    dataset_file = st.file_uploader("Upload a Custom Dataset(.csv)", type=["csv"])
    if dataset_file is not None:
        df = pd.read_csv(dataset_file)
        st.dataframe(df)
        st.button("Run Model Inference")

if __name__ == "__main__":
    main()