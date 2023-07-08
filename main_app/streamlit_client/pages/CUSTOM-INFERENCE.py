import streamlit as st
import pandas as pd
import requests
import os

def main():
    st.markdown("<h1 style= 'color: green;'>Custom Model Inference</h1>", unsafe_allow_html=True)
    dataset_file = st.file_uploader("Upload a Custom Dataset(.csv)", type=["csv"])
    url = "https://uploadfile.io/upload"
    # NEEDS SOME LOGIC FOR DATA AND WIDGET PERSISTANCE ON STREAMLIT
    # if 'dataset_file' not in st.session_state:
    #     st.session_state.dataset_file = pd.DataFrame()

    if dataset_file is not None:
        df = pd.read_csv(dataset_file)
        # st.session_state.dataset_file = df
        st.dataframe(df)
        # df.to_csv('custom.csv')
        submit = st.button("Run Model Inference")
        if submit:
            with open("./custom.csv", 'rb') as f:
                # response = requests.post(url, files={'file': f})
                res = requests.post(url, data=dataset_file)

            if os.path.exists("custom.csv"):
                os.remove("custom.csv")
            st.write(dir(res))    
            st.write(res.json()['link'])

    
if __name__ == "__main__":
    main()