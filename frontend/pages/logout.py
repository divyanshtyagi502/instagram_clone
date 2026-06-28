import streamlit as st

st.title("Logout")

if "token" in st.session_state:
    del st.session_state["token"]
    st.success("You have been logged out.")
    
else:
    st.info("You are not logged in.")    

