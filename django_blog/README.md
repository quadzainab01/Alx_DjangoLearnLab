Django Blog Project
Overview
This is a simple Django blog application that allows users to register, log in, manage profiles, and create, read, update, and delete (CRUD) blog posts.

Authenticated users can create, edit, and delete their own posts.

All users (authenticated or not) can view posts and post details.

Users have profile pages with editable bio and profile picture.

Features
1. Authentication
Register, login, and logout functionality.
User authentication enforced for creating and managing posts.
Passwords are securely stored using Django’s authentication system.

2. Profile Management
Users can update their username, email, bio, and profile picture.
Profiles are automatically created when a user registers.

3. Blog Post Management (CRUD)
ListView: View all posts at /posts/
DetailView: View individual post at /posts/<id>/
CreateView: Authenticated users can create a new post at /posts/new/
UpdateView: Authors can edit their own posts at /posts/<id>/edit/
DeleteView: Authors can delete their own posts at /posts/<id>/delete/

4. Permissions
Only logged-in users can create posts.
Only post authors can edit or delete their own posts.
All users can view the post list and details.

Installation
1. Clone the repository
bash:
git clone 
cd django_blog

2. Create and activate a virtual environment
bash:
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3. Install dependencies
bash:
pip install -r requirements.txt

4. Apply migrations
bash:
python manage.py makemigrations
python manage.py migrate

5. Create a superuser (optional, for admin access)
bash:
python manage.py createsuperuser

6. Run the development server
bash:
python manage.py runserver


Usage
1. Access the home page: http://127.0.0.1:8000/

2. Register a new account or login if you already have one.

3. Create posts:
Click "Create a New Post" (visible when logged in).
Enter title and content and submit.

4. Edit or delete posts:
Only your own posts will show "Edit" and "Delete" options.

5. Update profile:
Go to /profile/ to edit your bio, username, email, or profile picture.

6. Logout:
Click "Logout" in the navigation menu.

Project Structure:

blog/
├── migrations/
├── templates/blog/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── logout.html
│   ├── register.html
│   ├── profile.html
│   ├── post_list.html
│   ├── post_detail.html
│   ├── post_form.html
│   └── post_confirm_delete.html
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── signals.py
├── urls.py
└── views.py


Dependencies:
Django >= 4.0
Python >= 3.8

Notes:
Profile creation is automatic via signals.

Post permissions use LoginRequiredMixin and UserPassesTestMixin.

Pagination: Post list is paginated by 5 posts per page.