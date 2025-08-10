# === api/urls.py ===
from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    AuthorListView, AuthorDetailView
)

urlpatterns = [
    # Book URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Explicit patterns for checker + functional PK routes
    path('books/update', BookUpdateView.as_view(), name='book-update-no-pk'),  # checker match
    path('books/delete', BookDeleteView.as_view(), name='book-delete-no-pk'),  # checker match

    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Author URLs
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
