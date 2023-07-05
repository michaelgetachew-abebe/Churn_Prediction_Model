import streamlit as st

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

    elif choice == "Dataset":
        st.subheader("Dataset")

    elif choice == "DocumentFiles":
        st.subheader("Document Files")

    else:
        st.header("About")

    
if __name__ == "__main__":
    main()