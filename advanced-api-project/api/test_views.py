from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
<<<<<<< HEAD
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create authors
        self.author_a = Author.objects.create(name="Author A")
        self.author_b = Author.objects.create(name="Author B")

        # Create books linked to authors
        self.book1 = Book.objects.create(title="Book One", author=self.author_a, published_date="2001-01-01")
        self.book2 = Book.objects.create(title="Book Two", author=self.author_a, published_date="2002-01-01")
=======
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
>>>>>>> 08f5345f881e1b6eae852d2a07d2912d35b70987

    def test_list_books_authenticated(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_books_unauthenticated(self):
        self.client.credentials()  # Remove token
        url = reverse('book-list')
        response = self.client.get(url)
<<<<<<< HEAD
        self.assertEqual(response.status_code, status.HTTP_200_OK)
=======
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Allowed for all
>>>>>>> 08f5345f881e1b6eae852d2a07d2912d35b70987

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
<<<<<<< HEAD
        self.assertEqual(response.data['author']['id'], self.author_a.id)
=======
>>>>>>> 08f5345f881e1b6eae852d2a07d2912d35b70987

    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
<<<<<<< HEAD
            "author_id": self.author_b.id,  # Use author_id here
            "published_date": "2023-01-01"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author']['id'], self.author_b.id)
=======
            "author": self.author.pk,
            "publication_year": 2023
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
>>>>>>> 08f5345f881e1b6eae852d2a07d2912d35b70987

    def test_create_book_unauthenticated(self):
        self.client.credentials()  # Remove token
        url = reverse('book-create')
        data = {
            "title": "New Book",
<<<<<<< HEAD
            "author_id": self.author_b.id,
            "published_date": "2023-01-01"
        }
        response = self.client.post(url, data, format='json')
=======
            "author": self.author.pk,
            "publication_year": 2023
        }
        response = self.client.post(url, data)
>>>>>>> 08f5345f881e1b6eae852d2a07d2912d35b70987
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_update_book_authenticated(self):
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {
            "title": "Updated Title",
<<<<<<< HEAD
            "author_id": self.author_a.id,
            "published_date": "2005-01-01"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['author']['id'], self.author_a.id)
=======
            "author": self.author.pk,
            "publication_year": 2005
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
>>>>>>> 08f5345f881e1b6eae852d2a07d2912d35b70987

    def test_update_book_unauthenticated(self):
        self.client.credentials()  # Remove token
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {
            "title": "Updated Title",
<<<<<<< HEAD
            "author_id": self.author_a.id,
            "published_date": "2005-01-01"
        }
        response = self.client.put(url, data, format='json')
=======
            "author": self.author.pk,
            "publication_year": 2005
        }
        response = self.client.put(url, data)
>>>>>>> 08f5345f881e1b6eae852d2a07d2912d35b70987
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
<<<<<<< HEAD
        url = reverse('book-list') + f'?author={self.author_a.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['author']['id'] == self.author_a.id for book in response.data))
=======
        url = reverse('book-list') + f'?author={self.author.pk}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['author'] == self.author.pk for book in response.data))
>>>>>>> 08f5345f881e1b6eae852d2a07d2912d35b70987

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Two'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Book Two' in book['title'] for book in response.data))

<<<<<<< HEAD
    def test_order_books_by_published_date(self):
        url = reverse('book-list') + '?ordering=published_date'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dates = [book['published_date'] for book in response.data]
        self.assertEqual(dates, sorted(dates))
=======
    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
>>>>>>> 08f5345f881e1b6eae852d2a07d2912d35b70987
