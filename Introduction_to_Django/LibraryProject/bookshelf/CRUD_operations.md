# CRUD Operations Summary for Book Model (bookshelf app)

This file summarizes the Create, Retrieve, Update, and Delete operations performed on the `Book` model using the Django shell.

---

## ✅ Create a Book

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Output
1984 by George Orwell (1949)

---

## ✅ Retrieve a Book

from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

#Output:
1984 George Orwell 1949

---

## ✅ Update the Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

# Output:
Nineteen Eighty-Four


---

## ✅ Delete the Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())

# Output:
(<number>, {'bookshelf.Book': 1})
<QuerySet []>

