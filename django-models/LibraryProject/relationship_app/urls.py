from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('books/', views.list_books, name='book-list'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
