import streamlit as st
import pandas as pd
import requests

def main():
    st.markdown("<h1 style= 'color: green;'>Custom Model Inference</h1>", unsafe_allow_html=True)
    dataset_file = st.file_uploader("Upload a Custom Dataset(.csv)", type=["csv"])
    url = 'https://file.io'
    # NEEDS SOME LOGIC FOR DATA AND WIDGET PERSISTANCE ON STREAMLIT
    # if 'dataset_file' not in st.session_state:
    #     st.session_state.dataset_file = pd.DataFrame()

    if dataset_file is not None:
        df = pd.read_csv(dataset_file)
        st.dataframe(df)
        files = {'file': dataset_file.read()}        
        
        submit = st.button("Run Model Inference")
        if submit:
            response = requests.post('https://file.io', files=files)    
            st.write(response.json()['link'])

    
if __name__ == "__main__":
    main()