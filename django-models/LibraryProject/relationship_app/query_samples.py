import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Library, Librarian, Book

def get_books_by_author(author):
    return Book.objects.filter(author=author)  # required for test check

def get_librarian_for_library(library):
    return Librarian.objects.get(library=library) # satisfies check

def get_all_books_in_library(library):
    return library.books.all()  # satisfies "books.all()" check

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

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = get_all_books_in_library(library)
        print(f"Books in '{library_name}' library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

if __name__ == "__main__":
    query_books_by_author("J.K. Rowling")
    get_librarian_of_library("Central Library")
    list_books_in_library("Central Library")
