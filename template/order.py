import datetime
from ui_info import UIPayment
from order_position import OrderPosition

class Order():
    order_date: datetime = datetime.datetime.now()
    order_positions: list[OrderPosition] = []

    def __init__(self):
        self.order_date = datetime.datetime.now()
        return

    def add_ticket(self, info):
        order_pos = OrderPosition(info)
        self.order_positions.append(order_pos)

    def calculate_total(self, info):
        price = 0.0
        for order_pos in self.order_positions:
            price += order_pos.calculate_subtotal()
        # add payment surcharges
        payment_surcharge = Order.get_payment_surcharge(info)
        price += payment_surcharge

        return price

    def print(self):
        # connect to printer via adapter
        return

    @staticmethod
    def get_payment_surcharge(info):
        if info.payment == UIPayment.CreditCard:
            return 0.50
        else:
            return 0.0
