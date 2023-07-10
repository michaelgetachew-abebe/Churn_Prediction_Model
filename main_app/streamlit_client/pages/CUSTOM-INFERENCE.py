import streamlit as st
import pandas as pd
import requests
from sklearn.feature_extraction import DictVectorizer
import json
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.markdown("<h1 style= 'color: green;'>Custom Model Inference</h1>", unsafe_allow_html=True)
    dataset_file = st.file_uploader("Upload a Custom Dataset(.csv)", type=["csv"])
    url = 'http://127.0.0.1:9696/predict'
    dv  = DictVectorizer(sparse=False)
    categorical = ['gender', 'seniorcitizen', 'partner', 'dependents',
               'phoneservice', 'multiplelines', 'internetservice',
               'onlinesecurity', 'onlinebackup', 'deviceprotection',
               'techsupport', 'streamingtv', 'streamingmovies',
               'contract', 'paperlessbilling', 'paymentmethod']
    numerical = ['tenure', 'monthlycharges', 'totalcharges']
    # NEEDS SOME LOGIC FOR DATA AND WIDGET PERSISTANCE ON STREAMLIT
    # if 'dataset_file' not in st.session_state:
    #     st.session_state.dataset_file = pd.DataFrame()

    if dataset_file is not None:
        df = pd.read_csv(dataset_file)
        st.dataframe(df)

        df = df[categorical + numerical].to_dict(orient = 'records')
        dv.fit(df)

        df = dv.transform(df)
        
        # files = {'file': dataset_file.read()}        
        
        json_data = json.dumps(np.ndarray.tolist(df))
        submit = st.button("Run Model Inference")
        if submit:
            response = requests.post(url, json=json_data)    
            #st.write(dir(response))
            #st.write(type(response.json()))
            #st.write(response.json()['link'])
            #df = pd.json_normalize(response.json())
            df = pd.DataFrame(response.json())
            grouped_df = df.groupby('predictions').size().reset_index(name='counts')
            st.bar_chart(grouped_df)
            #st.write(df.shape)
            st.dataframe(df)

            fig1, ax1 = plt.subplots()
            ax1.pie(grouped_df['counts'], labels=['Non Churner','Churner'], autopct='%1.1f%%')
            ax1.axis('equal')

            st.pyplot(fig1)
if __name__ == "__main__":
    main()