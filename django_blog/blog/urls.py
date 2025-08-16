from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth
    path('login/',  auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Registration & Profile
    path('register/', views.register, name='register'),
    path('profile/',  views.profile, name='profile'),

    # (Optional) a simple home view you can add later
    path('', views.home, name='home'),
]
