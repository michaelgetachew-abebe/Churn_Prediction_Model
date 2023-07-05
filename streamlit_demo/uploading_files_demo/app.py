import streamlit as st

# File reader imports
from PIL import Image
from pandas import read_csv as Rcsv

# Image reader function
@st.cache
def read_image(image_file):
    image = Image.open(image_file)
    return image

# CSV reader function
@st.cache
def read_csv(dataset_file):
    dataset = Rcsv(dataset_file)
    return dataset

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
            # SEE THE TYPE OF THE FILE
            # st.write(type(dataset_file))

            # SEE THE DETAILS(ATTRIBUTES/METHODS) on the file
            # st.write(dir(dataset_file))

            file_details = {"filename": dataset_file.name, "filetype": dataset_file.type, "filesize": dataset_file.size}
            st.write(file_details)

            # READ THE Display the dataset on the streamlit UI
            st.write(read_csv(dataset_file))


    elif choice == "DocumentFiles":
        st.subheader("Document Files")

    else:
        st.header("About")

    
if __name__ == "__main__":
    main()