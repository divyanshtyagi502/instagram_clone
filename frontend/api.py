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
        "caption": caption
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