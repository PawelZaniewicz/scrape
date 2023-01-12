from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Plant
from .scrape import get_categories, get_urls, scrape_content_from_books


def index(request):
    plants = Plant.objects.all()
    return render(request, 'lista.html', {'plants': plants})


def books(request):
    url = "http://books.toscrape.com/index.html"
    cats = get_categories(url)
    links = get_urls(url)
    data = zip(cats, links)
    list_link = []
    for c, l in data:
        link = [c, l[25:-11], l]
        list_link.append(link)

    return render(request, 'scrape.html', {'data': data, 'list_link': list_link})


def book_details(request, book_cat):

    url = "http://books.toscrape.com/index.html"
    cats = get_categories(url)
    links = get_urls(url)
    data = zip(cats, links)
    list_link = []
    for c, l in data:
        link = [c, l[25:-11], l]
        list_link.append(link)

    for i in list_link:
        if i[1].lower() == book_cat.lower():
            selected_www = "http://books.toscrape.com/" + i[2]
            selected_category = i[0]
            continue
    book = scrape_content_from_books(selected_www)

    return render(request, 'book_details.html', {"book": book, "list_link": list_link, "selected_category": selected_category})
