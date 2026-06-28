import streamlit as st
from api import register_user

st.title("Register")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    response = register_user(
        username,
        email,
        password
    )

    if response.status_code == 200:
        st.success("Registration Successful!")

    else:
        st.error(response.json()["detail"])