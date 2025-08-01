"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-key-for-dev-only')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Replace with your production domain in deployment
ALLOWED_HOSTS = ['quadzainab01.pythonanywhere.com', '127.0.0.1', 'localhost']

# Added this comment to trigger a new commit for deployment check

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'csp',  # Added for Content Security Policy
]

MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',  # Content Security Policy middleware (must be high up)
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Added for production

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# ----------------------------------------
# ✅ Security Settings for Production
# ----------------------------------------

# Prevent XSS attacks
SECURE_BROWSER_XSS_FILTER = True

# Prevent MIME sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Clickjacking protection
X_FRAME_OPTIONS = 'DENY'

# Enforce HTTPS cookies
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Redirect all HTTP to HTTPS
SECURE_SSL_REDIRECT = True

# Use a secure referrer policy
SECURE_REFERRER_POLICY = 'strict-origin'

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 3600  # Increase to 31536000 (1 year) in production
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# ----------------------------------------
# ✅ Content Security Policy (CSP)

CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ("'self'",),
        'script-src': ("'self'", 'cdnjs.cloudflare.com'),
        'style-src': ("'self'", 'cdnjs.cloudflare.com'),
        'img-src': ("'self'", 'data:'),
        'font-src': ("'self'", 'fonts.gstatic.com'),
        'connect-src': ("'self'",),
    }
}

# --- HTTPS and Security Settings ---

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  # Enforce HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # One year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure cookies: Transmit only over HTTPS
SESSION_COOKIE_SECURE = True  # Protect session cookie
CSRF_COOKIE_SECURE = True     # Protect CSRF token cookie

# Additional security headers
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent content type sniffing
SECURE_BROWSER_XSS_FILTER = True    # Enable browser XSS filter
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DUMMY_SETTING_FOR_COMMIT = True

