from ui_info import UIPayment
from creditcard import CreditCard
from debitcard import DebitCard
from coin_machine import  IKEAMyntAtare2000

class Payment():
    @staticmethod
    def pay(info, price):
        if info.payment == UIPayment.CreditCard:
            c = CreditCard()
            c.connect()
            ccid: int = c.begin_transaction(round(price, 2))
            c.end_transaction(ccid)
            c.disconnect()
        elif info.payment == UIPayment.DebitCard:
            d = DebitCard()
            d.connect()
            dcid: int = d.begin_transaction(round(price, 2))
            d.end_transaction(dcid)
            d.disconnect()
        elif info.payment == UIPayment.Cash:
            coin = IKEAMyntAtare2000()
            coin.starta()
            coin.betala(int(round(price * 100)))
            coin.stoppa()