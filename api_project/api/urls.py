from django.urls import path
from .views import home, BookList

urlpatterns = [
    path('', home),
    path('books/', BookList.as_view(), name='book-list'),
]
