import streamlit as st

# File reader imports
from PIL import Image
import pandas as pd

# Handle Session Data
if 'dataset_file' not in st.session_state:
    st.session_state['dataset_file'] = ''
# Image reader function
@st.cache_resource
def read_image(image_file):
    image = Image.open(image_file)
    return image

# CSV reader function
@st.cache
def read_csv(dataset_file):
    dataset = pd.read_csv(dataset_file)
    return dataset

def ByteIO_to_FileWriter(byteIOfile):
    with open("file.csv", "wb") as f:
        f.write(byteIOfile.getvalue())

def main():
    st.title("File Upload")

    menu = ["Home", "Dataset", "DocumentFiles", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

        if image_file is not None:
            # SEE THE DETAILS OF THE FILE
            #file_type = type(image_file)
            #st.write(file_type)
            # SEE THE ATTRIBUTES/METHODS on the file
            
            # st.write(dir(image_file))
            file_details = {"filename":image_file.name, "filetype":image_file.type, "filesize":image_file.size}
            st.write(file_details)

            st.image(read_image(image_file))

    elif choice == "Dataset":
        st.subheader("Dataset")
        dataset_file = st.file_uploader("Upload a Custom Dataset", type=["csv"])

        if dataset_file is not None:
            st.write(type(dataset_file))
            file_details = {"filename": dataset_file.name, "filetype": dataset_file.type, "filesize": dataset_file.size}
            st.write(file_details)
            df = pd.read_csv(dataset_file)
            st.dataframe(df)
            # Logic: ByteIO -> LocalFile -> Read it while detecting the encoding mechanism -> Pass the encoding mechanism to read_csv method
            st.session_state['dataset_file'] = dataset_file

    elif choice == "DocumentFiles":
        st.subheader("Document Files")

    else:
        st.header("About")

    
if __name__ == "__main__":
    main()