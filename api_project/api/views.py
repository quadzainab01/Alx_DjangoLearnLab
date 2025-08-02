from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Home view (simple message)
def home(request):
    return JsonResponse({"message": "Hello from Django API!"})

# API view to list books
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
