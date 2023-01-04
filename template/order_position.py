from ticket import Ticket
class OrderPosition():
    quantity: int = 1
    ticket: Ticket

    def __init__(self, ticket):
        self.ticket = ticket
        #quantity is not set as there currently is no option for the user to buy multiple tickets at once
        return

    def calculate_subtotal(self):
        return self.quantity*self.ticket.get_ticket_price()