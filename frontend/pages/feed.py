import streamlit as st
from api import get_feed

st.title("Feed")

if "token" not in st.session_state:
    st.error("You must be logged in to view the feed.")
    st.stop()

response = get_feed(st.session_state["token"])

if response.status_code == 200:
    posts = response.json()
    for post in posts:
        st.write(f"**{post['username']}**: {post['caption']}")
        st.write(f"Owner ID: {post['owner_id']}")
        st.write(f"Likes: {post['likes_count']}")
        st.write(f"Comments: {post['comments_count']}")
else:
    st.error("Failed to fetch feed.")