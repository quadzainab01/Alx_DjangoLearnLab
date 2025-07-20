import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Library, Librarian

def get_books_by_author(author):
    # Returns a queryset of all books by the given author
    return author.books.all()

def get_books_in_library(library):
    # Returns a queryset of all books in the given library
    return library.books.all()

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

def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = get_books_in_library(library)
        print(f"Books in the library '{library_name}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

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
    query_books_by_author("J.K. Rowling")
    query_books_in_library("Central Library")
    get_librarian_of_library("Central Library")
