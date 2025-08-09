# Delete the Book instance

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())
