from ticket import Ticket, InternationalTicket, NationalTicket
from database import Database

class OrderPosition():
    quantity: int = 1
    ticket: Ticket

    def __init__(self, info):
        if info.to_station in Database.get_international_destinations():
            self.ticket = InternationalTicket(info)
        else:
            self.ticket = NationalTicket(info)
        # quantiy is a raw user input, if it's an int we'll use it, if not 1 is used instead 
        try:
            self.quantity = int(info.ticket_count)
        except:
            self.quantity = 1
        return

    def calculate_subtotal(self):
        return self.quantity * self.ticket.get_ticket_price()
