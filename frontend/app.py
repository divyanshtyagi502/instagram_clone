import streamlit as st

st.set_page_config(
    page_title="Instagram Clone",
    page_icon="📸",
    layout="wide"
)

st.title("📸 Instagram Clone MVP")

st.markdown("---")

if "token" in st.session_state:
    st.success("✅ Logged In")
else:
    st.warning("⚠️ Not Logged In")

st.markdown("""
## Welcome!

Use the sidebar to:

- Register
- Login
- Create Posts
- View Feed
- Logout
""")