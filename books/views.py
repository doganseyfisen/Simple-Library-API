from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"