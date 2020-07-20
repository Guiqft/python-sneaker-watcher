import requests
from bs4 import BeautifulSoup


def get_page(url):
    headers = {
        "User Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }

    r = requests.get(url, headers=headers)
    return BeautifulSoup(r.content, 'html.parser')


def get_qty_seach(page):
    result = page.find_all("p", class_="searchResultsTime")[
        0].find("span", class_="value")
    return int(result.text)


def get_sneakers_data(page):
    sneakers = page.find_all("div", class_="shelf-image")

    result = []
    for sneaker in sneakers:
        result.append(sneaker.find(
            "a", class_="shelf-image-link img-responsive"))

    return result


# AuthenticFeet URL
AF_URL = 'https://www.authenticfeet.com.br/masculino/tenis/41/air%20force?PS=24&map=c,c,specificationFilter_5,ft'
AF_page = get_page(AF_URL)

print(get_sneakers_data(AF_page))
