import streamlit as st

def load_image():
    uploaded_file = st.file_uploader(label="Pick an Image to Test")
    if uploaded_file is not None:
        image = uploaded_file.getvalue()
        st.image(image)

def main():
    st.title('Image(File) upload Demo')
    load_image()

if __name__ == "__main__":
    main()