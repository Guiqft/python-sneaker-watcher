import requests
from bs4 import BeautifulSoup
from decimal import Decimal


def get_page(url):
    if (url.find('busca.nike.com.br') == -1):
        headers = {
            "User Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        }

        r = requests.get(url, headers=headers)
        return BeautifulSoup(r.content, 'html.parser')

    else:
        r = requests.get(url)
        return r.content


def af_get_qty_seach(page):
    result = page.find_all("p", class_="searchResultsTime")[
        0].find("span", class_="value")
    return int(result.text)


def af_get_sneakers_data(page):
    sneakers = page.find_all(
        "li", class_="tenis-mochilas-e-acessorios-masculinos-|-authentic-feet last")

    result = []
    for sneaker in sneakers:
        t = sneaker.find("a", class_="shelf-image-link img-responsive")

        object = {
            "title": t.get('title'),
            "img_src": t.find("img").get('src'),
            "price": float(sneaker.find("span", class_="best-price").text.strip()[3:].replace(',', '.')),
            "url": t.get('href')
        }

        result.append(object)

    return result
