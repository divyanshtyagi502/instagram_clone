import streamlit as st
from api import get_profile

st.title("My Profile")

if "token" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

user_id = st.number_input(
    "User ID",
    min_value=1,
    value=1
)

if st.button("Load Profile"):

    response = get_profile(user_id)

    if response.status_code == 200:

        user = response.json()

        st.header(user["username"])

        st.write(f"Email: {user['email']}")
        st.write(f"Posts: {user['posts_count']}")
        st.write(f"Followers: {user['followers_count']}")
        st.write(f"Following: {user['following_count']}")

    else:

        st.error(response.text)