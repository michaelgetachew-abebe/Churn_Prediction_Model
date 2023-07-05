import streamlit as st

def main():
    st.title("File Upload")

    menu = ["Home", "Dataset", "DocumentFiles", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Dataset":
        st.subheader("Dataset")

    elif choice == "DocumentFiles":
        st.subheader("Document Files")

    else:
        st.header("About")

    
if __name__ == "__main__":
    main()