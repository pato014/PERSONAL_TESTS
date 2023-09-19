import pandas
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "The real Estate Company"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books a hotel by changing its availability to NO"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if Hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

    # Create a class method
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # create a magic method
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class Ticket(ABC):

    @abstractmethod
    def generate_ticket(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate_ticket(self):
        content = f"""Thank for your reservations!
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel: {self.hotel.name}
        """
        return content

    # Create a property
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    # Create a staticmethod
    @staticmethod
    def convert(amount):
        return amount * 1.2


class DigitalTicket(Ticket):

    def generate_ticket(self):
        return "Hello,  this is your digital ticekt"

    def download(self):
        pass
