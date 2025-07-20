from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, list_books, LibraryDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('', list_books, name='home'),  # optional home page
]
