from bs4 import BeautifulSoup
import requests, re

url = "http://books.toscrape.com/index.html"


def get_categories(url: str):
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    www_categories = soup.findAll("div", attrs={"class": "side_categories"})

    list_categories = []
    for row in www_categories:
        data = row.findAll("a")
        for n, val in enumerate(data):
            if n != 0:
                list_categories.append(val.text.strip())

    return list_categories


def get_urls(url: str):
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
    www_urls = soup.findAll("div", attrs={"class": "side_categories"})

    list_urls = []
    for row in www_urls:
        data = row.find_all('a', href=True)
        # print(data)
        for n, a in enumerate(data):
            if n != 0:
                list_urls.append((a['href']))

    return list_urls


def scrape_content_from_books(urls: str):
    page_to_scrape = requests.get(urls)
    soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

    book_name = soup.findAll("img")
    book_image = soup.findAll("img")
    book_price = soup.findAll("p", attrs={"class": "price_color"})
    book_url = soup.findAll("div", attrs={"class": "image_container"})

    l_book_name = []
    for row in book_name:
        data = row['alt']
        l_book_name.append(data)
    l_book_image = []
    for row in book_image:
        data2 = row['src']
        data2_ = "https://books.toscrape.com/" + data2[11:]
        l_book_image.append(data2_)
    l_book_price = []
    for row in book_price:
        data3 = row.text.strip()[1:]
        l_book_price.append(data3)
    l_book_url = []
    for row in book_url:
        data4 = row.find_all('a', href=True)
        for _ in data4:
            l_book_url.append(_['href'][9:])

    total = zip(l_book_name, l_book_image, l_book_price, l_book_url)

    return total
