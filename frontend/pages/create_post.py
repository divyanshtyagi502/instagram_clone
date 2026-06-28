import streamlit as st
from api import create_post

st.title("Create Post")

if "token" not in st.session_state:
    st.error("You must be logged in to create a post.")
    st.stop()
    
caption = st.text_area("Caption")    

if st.button("Create Post"):
    response = create_post(caption, st.session_state["token"])
    if response.status_code == 200:
        st.success("Post created successfully!")
    else:
        st.error(response.text)