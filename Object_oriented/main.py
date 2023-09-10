from operations import ops

URL = 'http://programmer100.pythonanywhere.com/tours/'
FILE_DIR = 'data.txt'


if __name__ == "__main__":
    event = ops.Event()
    scraped = event.scrape(URL)
    extracted = event.extract(scraped)
    print(extracted)
    db_ops = ops.DatabaseOps()
    content = ops.read(FILE_DIR)
    if extracted != "No upcoming tours" and extracted not in content:
        ops.store_in_file(extracted, FILE_DIR)
        ops.DatabaseOps.store_db(extracted)
        # email = ops.Email()
        # email.send(extracted, username="", password="", reciever="")
