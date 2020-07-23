from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader

from config import *

gmail_user = user_email
gmail_password = user_password
to_email = receiver_email


def send_mail(bodyContent, qty_sneaker):
    try:
        subject = "Actually are %s Air Force's avaiable at AuthenticFeet.com.br" % qty_sneaker

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
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('email.html')

    output = template.render(sneakers=sneakers)

    return output
