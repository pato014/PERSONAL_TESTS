import smtplib
import ssl

import requests
import selectorlib
from email.message import EmailMessage
from web_scrapping.conn import db_operations

def scrape(url):
    """Scrape the page source from the URL"""

    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    """Extract any exact fields from page"""

    extractor = selectorlib.Extractor.from_yaml_file("./extract.yaml")
    value = extractor.extract(source)['tours']
    return value


def send_email(message, username, password, reciever):
    """send mail when upcoming tour is available"""

    host = 'smtp.gmail.com'
    port = 465  # For SSL

    email_message = EmailMessage()
    email_message["Subject"] = "New tour is available"
    email_message.set_content(f"Hey, we just discovered new Tour in {message}!")
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, email_message.as_string())


def store_in_file(extracted, file_name):
    with open(file_name, 'a') as file:
        file.write(extracted + "\n")


def read(file_name):
    with open(file_name, 'r') as file:
        return file.read()


def store_db(data: str):
    list_data = [events for events in data.split(", ")]
    db_operations(list_data)


