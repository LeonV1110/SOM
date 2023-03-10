import datetime
from ui_info import UIInfo, UIClass, UIDiscount
from tariefeenheden import Tariefeenheden
from pricing_table import PricingTable
from exceptions import InvalidDestination
from abc import abstractmethod, ABC

class Ticket(ABC):
    travel_class: UIClass = UIClass.SecondClass
    international_train: bool = False  # uses international train | user input
    retour: bool = False
    from_station: str = ""
    to_station: str = ""
    ticket_date: datetime = datetime.datetime.now()
    discount: UIDiscount = UIDiscount.NoDiscount

    def __init__(self, info: UIInfo):
        self.travel_class = info.travel_class
        if info.way == 1:
            self.retour = False
        elif info.way == 2:
            self.retour = True
        self.from_station = info.from_station
        self.to_station = info.to_station
        if info.train_type == 1:
            self.international_train = False
        elif info.train_type == 2:
            self.international_train = True
        self.ticket_date == datetime.datetime.now()

    @abstractmethod
    def get_ticket_price(self):
        pass


class InternationalTicket(Ticket):
    def __init__(self, info: UIInfo):
        super().__init__(info)
        self.international_train = True

    def get_ticket_price(self):
        raise InvalidDestination(
            "This ticketmachine does not handle international journeys, please head over to the servicedesk")
        # place holder error msg


class NationalTicket(Ticket):
    def __init__(self, info: UIInfo):
        super().__init__(info)

    def get_ticket_price(self):
        # get number of tariefeenheden
        tariefeenheden: int = Tariefeenheden.get_tariefeenheden(self.from_station, self.to_station)

        # compute the column in the table based on choices and discounts
        table_column: int = self.__get_table_col__()

        # compute price using the table col
        price: float = PricingTable.get_price(tariefeenheden, table_column)

        # adjust price for retour or single
        if self.retour:
            price *= 2

        # add any ticket surcharges 
        ticket_surcharges = self.__get_ticket_surcharges__(price)
        price += ticket_surcharges

        return price

    def __get_ticket_surcharges__(self, price):
        if self.international_train: return price / 10  # 10% surcharge
        return 0.0  # return 0 as default

    def __get_table_col__(self):
        table_column = 0
        # compute the column in the table based on choices
        if self.travel_class == UIClass.FirstClass:
            table_column = 3

        # then, on the discount
        if self.discount == UIDiscount.TwentyDiscount:
            table_column += 1
        elif self.discount == UIDiscount.FortyDiscount:
            table_column += 2
        return table_column
