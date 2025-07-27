from django.urls import path
from .views import (
    list_books, add_book, edit_book, delete_book,
    register, LoginView, LogoutView,
    LibraryDetailView,
    admin_view, librarian_view, member_view
)

urlpatterns = [
    path('', list_books, name='list_books'),  # root page
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),

    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
