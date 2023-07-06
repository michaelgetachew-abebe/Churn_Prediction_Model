import streamlit as st
if 'count' not in st.session_state:
    st.session_state.count = 0

st.title('Sessions State Persisting(Counter)')

increment = st.button('Increment')

if increment:
    st.session_state.count += 1

decrement = st.button("Decrement")
if decrement:
    st.session_state.count += 1

st.write(st.session_state.count)