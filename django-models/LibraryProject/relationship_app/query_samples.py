import os
import django

# Set the correct settings module path for your project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author):
    # Returns a queryset of all books by the given author
    return Book.objects.filter(author=author)

def get_librarian_for_library(library):
    # Returns the librarian assigned to the given library
    return library.librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = get_books_by_author(author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

def get_librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = get_librarian_for_library(library)
        print(f"Librarian of '{library_name}' library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library '{library_name}'")

if __name__ == "__main__":
    # Change these sample names to match your database entries
    query_books_by_author("J.K. Rowling")
    get_librarian_of_library("Central Library")
