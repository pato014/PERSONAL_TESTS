from operations import ops

URL = 'http://programmer100.pythonanywhere.com/tours/'
FILE_DIR = 'data.txt'



if __name__ == "__main__":
    scraped = ops.scrape(URL)
    extracted = ops.extract(scraped)
    print(extracted)

    content = ops.read(FILE_DIR)
    if extracted != "No upcoming tours" and extracted not in content:
        ops.store_in_file(extracted, FILE_DIR)
        ops.store_db(extracted)
        ops.send_email(extracted, username="", password="", reciever="")
