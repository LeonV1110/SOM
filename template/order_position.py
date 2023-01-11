from ticket import Ticket


class OrderPosition():
    quantity: int = 1
    ticket: Ticket

    def __init__(self, ticket, quantity):
        self.ticket = ticket
        # quantiy is a raw user input, if it's an int we'll use it, if not 1 is used instead
        try:
            self.quantity = int(quantity)
        except:
            self.quantity = 1

        return

    def calculate_subtotal(self):
        return self.quantity * self.ticket.get_ticket_price()
