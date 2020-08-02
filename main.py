from scraper import get_page, af_get_qty_seach, af_get_sneakers_data
from mail_sender import fill_email_template, send_mail
import json


def send_authenticFeet_email():
    # AuthenticFeet URL
    AF_URL = 'https://www.authenticfeet.com.br/masculino/tenis/41/air%20force?PS=24&map=c,c,specificationFilter_5,ft'

    # Getting all the AuthenticFeet page and dealing using BeutifulSoup
    AF_page = get_page(AF_URL)  # Getting all data

    # Spliting data to get what we want
    AF_qty_sneaker = af_get_qty_seach(AF_page)
    AF_sneakers = af_get_sneakers_data(AF_page)

    # Filling email template and sending it
    AF_email_body = fill_email_template(AF_sneakers)
    send_mail(AF_email_body, AF_qty_sneaker, 0)


def send_nike_email():
    # For Nike, we can use the API and get the Json response, so we don't need BeutifulSoup
    NIKE_SEARCH_ROUTE = 'https://busca.nike.com.br/busca?q=air%20force&origin=autocomplete&common_filter%5B372%5D=3257&sort=5&ajaxSearch=1'
    NIKE_json_response = json.loads(
        get_page(NIKE_SEARCH_ROUTE))  # Getting all data

    # Spliting data to get what we want
    NIKE_qty_sneaker = NIKE_json_response["totalProducts"]["totalResults"]
    NIKE_sneakers = NIKE_json_response["productsInfo"]["products"]

    # Filling email template and sending it
    NIKE_email_body = fill_email_template(NIKE_sneakers)
    send_mail(NIKE_email_body, NIKE_qty_sneaker, 1)


send_nike_email()
