from django.urls import path
from .views import BookListView

"""
Assigns the name "home" to the URL pattern for BookListView. This naming allows for dynamic referencing of this URL pattern in Django using reverse() or redirect() functions.
"""

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
]

