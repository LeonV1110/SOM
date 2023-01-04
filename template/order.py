import datetime
from ui_info import UIPayment
class Order():
    order_date: datetime = datetime.datetime.now()
    order_positions: list = []

    def __init__(self, order_positions):
        self.order_date = datetime.datetime.now()
        self.order_positions = order_positions
        return
    
    def add_order_pos(self, order_pos):
        self.order_positions.append(order_pos)

    def calculate_total(self, info):
        price = 0.0
        for order_pos in self.order_positions:
            price += order_pos.calculate_subtotal()
        #add payment surcharges
        payment_surcharge = Order.get_payment_surcharge(info)
        price += payment_surcharge

        return price

    @staticmethod
    def get_payment_surcharge(info):
        if info.payment == UIPayment.CreditCard:
            return 0.50
        else: return 0.0