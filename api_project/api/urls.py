from django.urls import path
from .views import home, BookList

urlpatterns = [
    path('', home, name='home'),                # Will return {"message": "Hello from Django API!"}
    path('books/', BookList.as_view(), name='book-list'),  # Will return the JSON list of books
]
