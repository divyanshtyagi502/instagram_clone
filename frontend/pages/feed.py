import streamlit as st
from api import (
    get_feed,
    like_post,
    get_comments,
    add_comment
)

st.title("Your Feed")


if "token" not in st.session_state:
    st.error("Please login first.")
    st.stop()


response = get_feed(st.session_state["token"])

if response.status_code != 200:
    st.error(response.text)
    st.stop()

posts = response.json()

if not posts:
    st.info("No posts available.")
    st.stop()


for post in posts:

    with st.container():

        st.markdown(f" {post['caption']}")
        st.caption(f"Posted by: {post['owner']['username']}")


        st.write(f"❤️ Likes: {post['likes_count']}")

        st.write(f"💬 Comments: {post['comments_count']}")

        
        if "likes_count" in post:
            st.write(f"❤️ {post['likes_count']} Likes")

      
        if st.button("❤️ Like", key=f"like_{post['id']}"):

            like_response = like_post(
                post["id"],
                st.session_state["token"]
            )

            if like_response.status_code == 200:
                st.success("Post liked!")
                st.rerun()
            else:
                st.error(like_response.text)

        st.markdown("Comments")

        comments_response = get_comments(post["id"], st.session_state["token"])

        if comments_response.status_code == 200:

            comments = comments_response.json()

            if comments:
                for comment in comments:
                    st.write(f"• {comment['content']}")
            else:
                st.write("No comments yet.")

        else:
            st.error("Couldn't load comments.")

        new_comment = st.text_input(
            "Write a comment",
            key=f"comment_{post['id']}"
        )

        if st.button(
            "Add Comment",
            key=f"comment_btn_{post['id']}"
        ):

            if new_comment.strip() == "":
                st.warning("Comment cannot be empty.")

            else:

                comment_response = add_comment(
                    post["id"],
                    new_comment,
                    st.session_state["token"]
                )

                if comment_response.status_code == 200:
                    st.success("Comment added!")
                    st.rerun()
                else:
                    st.error(comment_response.text)

        st.divider()