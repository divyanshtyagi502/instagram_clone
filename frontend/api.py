import requests
from config import BACKEND_URL


def register_user(username, email, password):
    url = f"{BACKEND_URL}/register"

    data = {
        "username": username,
        "email": email,
        "password": password
    }

    response = requests.post(url, json=data)

    return response

def login_user(username, password):
    url = f"{BACKEND_URL}/login"

    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, data=data)

    return response

def create_post(caption, token):
    url = f"{BACKEND_URL}/posts"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "caption": caption,
        "image_url": "https://example.com/image.jpg"  
    }

    response = requests.post(
        url,
        json=data,
        headers=headers
    )

    return response

def get_feed(token):
    url = f"{BACKEND_URL}/feed"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        url,
        headers=headers
    )

    return response

def like_post(post_id, token):
    url = f"{BACKEND_URL}/posts/{post_id}/like"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(
        url,
        headers=headers
    )

    return response

def get_comments(post_id, token):
    url = f"{BACKEND_URL}/comments/posts/{post_id}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    return response

def add_comment(post_id, content, token):
    url = f"{BACKEND_URL}/comments/posts/{post_id}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "content": content
    }

    response = requests.post(
        url,
        json=data,
        headers=headers
    )

    return response

def get_profile(user_id):
    url = f"{BACKEND_URL}/{user_id}"
    return requests.get(url)

def get_me(token):

    url = f"{BACKEND_URL}/me"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.get(
        url,
        headers=headers
    )