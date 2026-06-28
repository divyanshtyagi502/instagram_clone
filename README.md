# 📸 Instagram Clone MVP

A backend-focused Instagram Clone built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT Authentication**, with a lightweight **Streamlit** frontend to demonstrate the API functionality.

---

## 🚀 Features

### Authentication

* User Registration
* User Login
* JWT Authentication
* Protected Routes

### Posts

* Create Post
* View All Posts
* View Single Post
* Delete Own Post
* Personalized Feed

### Likes

* Like a Post
* Prevent Duplicate Likes

### Comments

* Add Comment
* View Comments
* Delete Own Comment

### User Profiles

* View Own Profile
* View Other User Profiles
* View User Posts

### Follow System

* Follow Users
* Unfollow Users
* View Followers
* View Following

### Frontend

* Login
* Register
* Feed
* Create Post
* Profile Page

---

# 🛠️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy ORM
* PostgreSQL
* Pydantic
* JWT Authentication
* Uvicorn

### Frontend

* Streamlit

### Database

* PostgreSQL

---

# 📁 Project Structure

```
instagram_clone/

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── main.py
│   ├── requirements.txt
│   └── venv/

├── frontend/
│   ├── pages/
│   ├── api.py
│   ├── config.py
│   ├── home.py
│   ├── requirements.txt
│   └── venv/

└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/divyanshtyagi502/instagram_clone.git
```

```
cd instagram_clone
```

---

## 2. Backend Setup

```
cd backend
```

Create virtual environment

```
python -m venv venv
```

Activate

### Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run FastAPI

```
uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger Docs

```
http://127.0.0.1:8000/docs
```

---

## 3. Frontend Setup

Open another terminal

```
cd frontend
```

Create virtual environment

```
python -m venv venv
```

Activate

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run Streamlit

```
streamlit run home.py
```

---

# 📌 API Endpoints

## Authentication

| Method | Endpoint  | Description   |
| ------ | --------- | ------------- |
| POST   | /register | Register User |
| POST   | /login    | Login User    |
| GET    | /me       | Current User  |

---

## Posts

| Method | Endpoint         |
| ------ | ---------------- |
| POST   | /posts           |
| GET    | /posts           |
| GET    | /posts/{post_id} |
| DELETE | /posts/{post_id} |
| GET    | /feed            |

---

## Likes

| Method | Endpoint              |
| ------ | --------------------- |
| POST   | /posts/{post_id}/like |

---

## Comments

| Method | Endpoint                  |
| ------ | ------------------------- |
| POST   | /comments/posts/{post_id} |
| GET    | /comments/posts/{post_id} |
| DELETE | /comments/{comment_id}    |

---

## Follow

| Method | Endpoint                    |
| ------ | --------------------------- |
| POST   | /follow/{user_id}           |
| DELETE | /follow/{user_id}           |
| GET    | /follow/followers/{user_id} |
| GET    | /follow/following/{user_id} |

---

## User

| Method | Endpoint         |
| ------ | ---------------- |
| GET    | /{user_id}       |
| GET    | /{user_id}/posts |

---


# Future Improvements

* Image Upload Support
* Search Users
* Edit Profile
* Edit/Delete Comments
* Pagination
* Notifications
* Docker Deployment
* Unit Tests
* CI/CD Pipeline

---

# Author

**Divyansh Tyagi**

---

# License

This project is developed for educational purposes.
