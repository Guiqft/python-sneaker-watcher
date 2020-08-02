from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import json

from config import *

gmail_user = user_email
gmail_password = user_password
to_email = receiver_email


def send_mail(bodyContent, qty_sneaker, origin_selector):
    try:
        # origin_selector tell us if are authenticfeet or nike
        if (origin_selector == 0):
            subject = "Actually are %s Air Force's avaiable at AuthenticFeet.com.br" % qty_sneaker
        elif (origin_selector == 1):
            subject = "Actually are %s Air Force's avaiable at Nike.com.br" % qty_sneaker

        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = gmail_user
        message['To'] = to_email

        message.attach(MIMEText(bodyContent, "html"))
        msgBody = message.as_string()

        server = SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msgBody)
        server.quit()

        print('Email sent!')
    except Exception as e:
        print(e)


def fill_email_template(sneakers):
    # loading html email template
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('email.html')

    sneakers_object = []

    for sneaker in sneakers:
        # try to fill with AuthenticFeet object
        try:
            temp_object = {
                "title": sneaker["title"],
                "img_src": sneaker["img_src"],
                "price": sneaker["price"],
                "url": sneaker["url"]
            }
        # if fail, try to fill with Nike object
        except:
            temp_object = {
                "title": sneaker["name"],
                "img_src": "https:" + sneaker["imageUrl"],
                "price": sneaker["discountedPriceRaw"],
                "url": "https:" + sneaker["productUrl"]
            }

        sneakers_object.append(temp_object)

    # generating filled html email
    output = template.render(sneakers=sneakers_object)

    return output
