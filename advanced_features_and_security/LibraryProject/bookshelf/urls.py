from django.urls import path
from .views import (
    BookListView, BookCreateView, BookUpdateView, BookDeleteView,
    search_books  # ✅ Add this
)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('search/', search_books, name='book_search'),  # ✅ Added search view
]
