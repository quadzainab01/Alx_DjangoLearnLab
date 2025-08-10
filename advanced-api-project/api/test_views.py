from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Author, Book
from datetime import date


class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for login
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # Login for session-based authentication
        self.client.login(username="testuser", password="testpass123")

        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create some books
        self.book1 = Book.objects.create(
            title="First Book",
            author=self.author1,
            publication_date=date(2020, 5, 17)
        )
        self.book2 = Book.objects.create(
            title="Second Book",
            author=self.author2,
            publication_date=date(2021, 6, 20)
        )

        self.book_list_url = reverse("book-list")

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_date": "2023-01-01"
        }
        response = self.client.post(self.book_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "author": self.author1.id,
            "publication_date": "2020-05-17"
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        response = self.client.get(self.book_list_url, {"title": "First Book"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.book_list_url, {"search": "First"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_desc(self):
        response = self.client.get(self.book_list_url, {"ordering": "-publication_date"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Second Book")
