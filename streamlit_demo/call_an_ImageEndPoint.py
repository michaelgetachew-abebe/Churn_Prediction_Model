import streamlit as st
import requests

def fetch(session, url):
    try:
        result = session.get(url)
        return result
    except Exception:
        return {}
    
def main():
    st.set_page_config("Image viewer page")
    st.title("Image Viewer Demo Page")
    session = requests.Session()
    with st.form("my-form"):
        index = st.number_input("ID", min_value=0, max_value=100, key="index")
        submitted=st.form_submit_button("Submit")

        if submitted:
            st.write("Result")
            data = fetch(session, f"https://picsum.photos/id/{index}/info")
            if data:
                st.image(data['download_url'], caption=f"Author: {data['author']}")
            else:
                st.error("Error")

if __name__ == "__main__":
    main()