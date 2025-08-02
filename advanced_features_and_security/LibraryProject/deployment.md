# Django Deployment Guide

---

## 🔧 Local Development Setup (Windows + Git Bash + VS Code)

# Clone the Repository
   ```bash
   git clone https://github.com/quadzainab01/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/advanced_features_and_security/LibraryProject

# Create and Activate a Virtual Environment
python -m venv venv
source venv/Scripts/activate

# Install Dependencies
pip install -r requirements.txt

# Apply Migrations
python manage.py makemigrations
python manage.py migrate

# Create a Superuser
python manage.py createsuperuser

# Run Development Server
python manage.py runserver