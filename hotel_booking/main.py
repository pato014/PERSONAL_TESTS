import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
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


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate_ticket(self):
        content = f"""Thank for your reservations!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


print(df)
hotel_id = input("Enter Id of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name please: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate_ticket())
else:
    print("Hotel is not free")
