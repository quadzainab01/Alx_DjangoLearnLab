# Alx_DjangoLearnLab

A learning repository for practicing **Django** concepts, including building a social media API, authentication, and other web development features.

## 🚀 Features
- Django-based backend
- Social media API
- User authentication & authorization
- REST framework integration
- Admin dashboard

## 📂 Project Structure
social_media_api/
├── social_media_api/          # Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/                  # Custom app for user 
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py              # CustomUser model
│   ├── serializers.py         # User registration/login 
│   ├── views.py               # Views for registration/login
│   ├── urls.py                # URLs for accounts endpoints
│
├── manage.py                  # Django management script
├── db.sqlite3                 # SQLite database (created after migrations)
├── requirements.txt           # List of dependencies (optional)
└── venv/                      # Virtual environment folder


## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/quadzainab01/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/social_media_api

2.  Create and activate a virtual environment:
    python -m venv venv
    source venv/Scripts/activate      # For Bash

3.  Install dependencies:
    pip install -r requirements.txt

4.  Apply migrations:
    python manage.py migrate

5.  Create a superuser:
    python manage.py createsuperuser

6.  Run the server:
    python manage.py runserver

7.  Visit the app:
    API: http://127.0.0.1:8000/api/

    Admin: http://127.0.0.1:8000/admin/


User Model Overview
CustomUser extends Django’s AbstractUser and includes:

1.  bio (TextField) – user biography

2.  profile_picture (ImageField) – optional profile photo followers (ManyToManyField) – allows users to follow others


🛠️ Tools & Tech
1.  Python 3
2.  Django
3.  Django REST Framework
4.  SQLite (default, can be replaced with PostgreSQL/MySQL)
5.  Git Bash
6.  Vs Code

✍️ Author: Zainab Abiola Quadri
📌 Goal: Practice and master Django web development.