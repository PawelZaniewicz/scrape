from django.urls import path
from startujemy.views import index
from startujemy.views import books
from startujemy.views import book_details

urlpatterns = [
    path('wytwornie', index, name='index'),
    path('scrape', books, name='books'),
    path("<str:book_cat>", book_details, name='book_details'),

]