from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Ordinary Title",
            subtitle = "A Boring Subtitle",
            author = "Who Dis",
            isbn = "1122334455667",
        )

    # Post
    def test_book_content(self):
        self.assertEqual(self.book.title, "Ordinary Title")
        self.assertEqual(self.book.subtitle, "A Boring Subtitle")
        self.assertEqual(self.book.author, "Who Dis")
        self.assertEqual(self.book.isbn, "1122334455667")

    # Get
    def test_book_listview(self):
        # "home" -> books/urls.py
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Boring Subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
        