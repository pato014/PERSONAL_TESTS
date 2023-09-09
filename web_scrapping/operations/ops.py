import requests
import selectorlib
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


def send_email():
    """send mail when upcoming tour is available"""

    print("email sent")


def store(extracted, file_name):
    with open(file_name, 'a') as file:
        file.write(extracted + "\n")


def read(file_name):
    with open(file_name, 'r') as file:
        return file.read()
