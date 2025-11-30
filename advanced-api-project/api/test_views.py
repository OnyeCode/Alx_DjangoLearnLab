from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.contrib.auth.models import User

from .models import Book, Author


class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user for authenticated tests
        self.user = User.objects.create_user(
            username="tester",
            password="password123"
        )

        # Create author
        self.author = Author.objects.create(name="John Doe")

        # Create sample books
        self.book1 = Book.objects.create(
            title="Alpha",
            publication_year=2020,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Beta",
            publication_year=2022,
            author=self.author
        )

        self.client = APIClient()

        # Endpoints
        self.list_url = reverse("books-list")
        self.detail_url = reverse("books-detail", kwargs={"pk": self.book1.pk})
        self.create_url = reverse("books-create")
        self.update_url = reverse("books-update", kwargs={"pk": self.book1.pk})
        self.delete_url = reverse("books-delete", kwargs={"pk": self.book2.pk})

    # -------------------- LIST VIEW TESTS --------------------

    def test_list_books(self):
        """Test retrieving all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books(self):
        """Test filtering by title"""
        response = self.client.get(self.list_url, {"title": "Alpha"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Alpha")

    def test_search_books(self):
        """Test searching across fields"""
        response = self.client.get(self.list_url, {"search": "Beta"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Beta")

    def test_order_books(self):
        """Test ordering"""
        response = self.client.get(self.list_url, {"ordering": "title"})
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, ["Alpha", "Beta"])

    # -------------------- CREATE VIEW TEST --------------------

    def test_create_book_authenticated(self):
        """Authenticated users can create books"""
        self.client.login(username="tester", password="password123")
        data = {
            "title": "Gamma",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users should not create books"""
        data = {
            "title": "Delta",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -------------------- DETAIL VIEW TEST --------------------

    def test_get_single_book(self):
        """Retrieve a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha")

    # -------------------- UPDATE VIEW TEST --------------------

    def test_update_book_authenticated(self):
        """Authenticated users can update books"""
        self.client.login(username="tester", password="password123")
        data = {
            "title": "Alpha Updated",
            "publication_year": self.book1.publication_year,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Alpha Updated")

    def test_update_book_unauthenticated(self):
        """Unauthenticated users cannot update"""
        data = {"title": "Fail Update", "publication_year": 2020, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -------------------- DELETE VIEW TEST --------------------

    def test_delete_book_authenticated(self):
        """Authenticated users can delete books"""
        self.client.login(username="tester", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """Unauthenticated users cannot delete"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

