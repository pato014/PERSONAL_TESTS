import smtplib
import ssl

import requests
import selectorlib
from email.message import EmailMessage
from Object_oriented.conn import DB


class Event:
    def scrape(self, url):
        """Scrape the page source from the URL"""

        response = requests.get(url)
        source = response.text
        return source

    def extract(self, source):
        """Extract any exact fields from page"""

        extractor = selectorlib.Extractor.from_yaml_file("./extract.yaml")
        value = extractor.extract(source)['tours']
        return value


class Email:
    def send(self, message, username, password, reciever):
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
        print("Email has been sent")


def store_in_file(extracted, file_name):
    with open(file_name, 'a') as file:
        file.write(extracted + "\n")


def read(file_name):
    with open(file_name, 'r') as file:
        return file.read()


class DatabaseOps:
    def __init__(self):
        self.db_ops = DB()

    def store_db(self, data: str):
        store = self.db_ops.store()
        list_data = [events for events in data.split(", ")]
        store(list_data)

    def read_db(self, data: str):
        list_data = [events for events in data.split(", ")]
        row = self.db_ops.read(list_data)
        return row

