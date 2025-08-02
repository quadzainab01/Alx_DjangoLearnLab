from django.http import JsonResponse
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Home view (simple message)
def home(request):
    return JsonResponse({"message": "Hello from Django API!"})

# API view to list books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
