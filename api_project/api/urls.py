from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, BookList, BookViewSet

# Create and register router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', home, name='home'),  # Root: http://127.0.0.1:8000/
    path('books/', BookList.as_view(), name='book-list'),  # http://127.0.0.1:8000/books/

    # Include router URLs (CRUD: /books_all/, /books_all/<id>/, etc.)
    path('', include(router.urls)),
]
