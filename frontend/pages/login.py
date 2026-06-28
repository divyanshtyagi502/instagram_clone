import streamlit as st
from api import get_me, login_user

st.title("Login")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    response = login_user(
        username,
        password
    )

    if response.status_code == 200:

        token = response.json()["access_token"]

        st.session_state["token"] = token

        st.success("Login Successful!")
        
        token = response.json()["access_token"]

        st.session_state["token"] = token
        st.session_state["username"] = username
        me = get_me(token).json()

        st.session_state["id"] = me["id"]
        st.session_state["username"] = me["username"]
        st.session_state["email"] = me["email"]

    else:

        st.error("Invalid Credentials")
 
st.write(st.session_state)       