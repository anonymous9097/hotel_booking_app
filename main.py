import pandas

df = pandas.read_csv("hotels.csv")


class Hotel:
    def __init__(self):
        pass

    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
id = input("Enter ID of the Hotel: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())