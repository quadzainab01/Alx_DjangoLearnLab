from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create user and token
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)

        # Setup API client and authenticate with token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create Author instance
        self.author = Author.objects.create(name="Author A")

        # Create Book instances
        self.book1 = Book.objects.create(title="Book One", author=self.author, publication_year=2001)
        self.book2 = Book.objects.create(title="Book Two", author=self.author, publication_year=2002)

    def test_list_books_authenticated(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_books_unauthenticated(self):
        self.client.credentials()  # Remove token
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Allowed for all

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "author": self.author.pk,
            "publication_year": 2023
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_create_book_unauthenticated(self):
        self.client.credentials()  # Remove token
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "author": self.author.pk,
            "publication_year": 2023
        }
        response = self.client.post(url, data)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_update_book_authenticated(self):
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {
            "title": "Updated Title",
            "author": self.author.pk,
            "publication_year": 2005
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_update_book_unauthenticated(self):
        self.client.credentials()  # Remove token
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {
            "title": "Updated Title",
            "author": self.author.pk,
            "publication_year": 2005
        }
        response = self.client.put(url, data)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_delete_book_authenticated(self):
        url = reverse('book-delete', kwargs={'pk': self.book2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book_unauthenticated(self):
        self.client.credentials()  # Remove token
        url = reverse('book-delete', kwargs={'pk': self.book2.pk})
        response = self.client.delete(url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_filter_books_by_author(self):
        url = reverse('book-list') + f'?author={self.author.pk}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['author'] == self.author.pk for book in response.data))

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Two'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Book Two' in book['title'] for book in response.data))

    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
