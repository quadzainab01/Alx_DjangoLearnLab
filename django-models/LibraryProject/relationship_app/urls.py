from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, CustomLoginView, CustomLogoutView, list_books, LibraryDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('', list_books, name='home'),
]
