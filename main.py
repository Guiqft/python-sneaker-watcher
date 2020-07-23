from scraper import get_page, get_qty_seach, get_sneakers_data
from mail_sender import fill_email_template, send_mail

# AuthenticFeet URL
AF_URL = 'https://www.authenticfeet.com.br/masculino/tenis/41/air%20force?PS=24&map=c,c,specificationFilter_5,ft'
AF_page = get_page(AF_URL)

qty_sneaker = get_qty_seach(AF_page)
sneakers = get_sneakers_data(AF_page)

email_body = fill_email_template(sneakers)
send_mail(email_body, qty_sneaker)
