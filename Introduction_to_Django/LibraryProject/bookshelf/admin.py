from django.contrib import admin

# Register your models here.
from .models import Book  # Import the Book model

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in the admin list view
    list_filter = ('publication_year',)  # Filter by publication year
    search_fields = ('title', 'author')  # Enable search by title and author
