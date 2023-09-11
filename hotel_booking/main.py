import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_card = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)

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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {
            "number": self.number,
            "expiration": expiration,
            "holder": holder,
            "cvc": cvc
        }
        if card_data in df_card:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_passwords):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_passwords:
            return True
        else:
            return False


print(df)
hotel_id = input("Enter Id of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.available():
    card_number = input("please enter you card number: ")
    credit_card = SecureCreditCard(number=card_number)
    if credit_card.validate(expiration="12/26", holder="NIKA PATO", cvc="234"):
        given_password = input("Enter your car password: ")
        if credit_card.authenticate(given_password):
            hotel.book()
            name = input("Enter your name please: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate_ticket())
        else:
            print("Credit card authentication failed")
    else:
        print("There was a problem with your payment!!!")
else:
    print("Hotel is not free")
