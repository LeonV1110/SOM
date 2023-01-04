import datetime
from ui_info import UIInfo, UIClass, UIDiscount
from tariefeenheden import Tariefeenheden
from pricing_table import PricingTable
from exceptions import InvalidDestination

class Ticket():
    travel_class: UIClass = UIClass.SecondClass
    international: bool = False #internation destination | set if the destination is international
    international_train: bool = False #uses international train | user input
    retour: bool = False
    from_station: str = ""
    to_station: str = ""
    ticket_date: datetime = datetime.datetime.now()
    discount: UIDiscount = UIDiscount.NoDiscount

    def __init__(self, info: UIInfo):
        #international_destinations = [] #TODO should be an value read from database
        self.travel_class = info.travel_class
        if info.way == 1: self.retour = False
        elif info.way == 2: self.retour = True
        self.from_station = info.from_station
        self.to_station = info.to_station
        """if self.to_station in international_destinations: #TODO fix later!!
            self.international = True
            self.international_train = True"""
        #date, international and international_train are not initiated as here as these are not present in the UI

    #throws InvalidDestination exception if there is an 
    def get_ticket_price(self):
        #if self.international: raise InvalidDestination() #TODO see TODO above

        # get number of tariefeenheden
        tariefeenheden: int = Tariefeenheden.get_tariefeenheden(self.from_station, self.to_station)

        # compute the column in the table based on choices
        table_column = 0
        if self.travel_class == UIClass.FirstClass:
            table_column = 3
        
        # then, on the discount
        if self.discount == UIDiscount.TwentyDiscount:
            table_column += 1
        elif self.discount == UIDiscount.FortyDiscount:
            table_column += 2

		# compute price
        price: float = PricingTable.get_price (tariefeenheden, table_column)
        if self.retour:
            price *= 2
        
        # add any ticket surcharges 
        ticket_surcharges = self.get_ticket_surcharges(price)
        price += ticket_surcharges

        return price
    
    def get_ticket_surcharges(self, price):
        if self.international_train: return price/10 #10% surcharge
        return 0.0
    