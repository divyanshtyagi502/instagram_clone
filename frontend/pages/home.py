import streamlit as st

st.set_page_config(page_title="Instagram Clone", page_icon="📸")

st.title("📸 Instagram Clone")

if "token" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

username = st.session_state.get("username", "User")

st.success(f"Welcome {username}!")

st.write("### Features")
st.write("✅ Feed")
st.write("✅ Create Post")
st.write("✅ Profile")

if st.button("Logout"):
    st.session_state.clear()
    st.success("Logged out successfully.")
    st.switch_page("home.py")