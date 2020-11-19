"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd
import datetime
#import cv2
from customer_simulation import Customer
#from animation_template import SupermarketMap, MARKET


transition_matrix = pd.read_csv("data/transition_matrix.csv")
transition_matrix.set_index("location", inplace=True)


class Supermarket():
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self):
        # a list of Customer objects
        self.customers = []  # here we need the Customer class!
        self.minutes = 0  # how many minutes have passed?
        self.last_id = 0  # we can concatenate it with the id from customer
        self.possible_states = 5  # or list of locations?
        self.current_time = 0  # current supermarket time

    def __repr__(self):
        # should return :
        # - customers, state (path) of customers,current time, time elapsed
        return f'Supermarket("{self.customers}", "{self.current_time}")'

    def get_time(self):
        """current time in HH:MM format,
        """
        # now = datetime.now().time() #creates a time object
        now = datetime.datetime.now()
        self.current_time = now  # .strftime("%H:%M")

    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        # current time --> supermarket
        # customer.state --> from customers
        # customer.id --> Customer
        return f'Supermarket("{self.customers}", "{self.current_time}")'

    def next_minute(self):
        """propagates all customers to the next state.
        """
        self.current_time += datetime.timedelta(minutes=1)
        self.minutes += 1
        # we would need to call a next_state on customers
        # I do not know how to access it to print it????
        for cust in self.customers:
            cust.next_state()

    def add_new_customers(self, stop):
        """randomly creates new customers.
        """
        for i in range(stop):
            cust = Customer(i, "entrance", transition_matrix)
            self.customers.append(cust)

    def remove_existing_customers(self):
        """removes every customer that is not active any more.
        """
        # remove the customers which are not active (.is_active )

        for cust in self.customers:
            if cust.state == 'checkout':
                self.customers.remove(cust)
                print(f'{cust } removed')


if __name__ == '__main__':

    penny = Supermarket()
    penny.get_time()
    penny.add_new_customers(2)
    print(penny.print_customers())
    penny.next_minute()
    print(penny.print_customers())
    penny.next_minute()
    print(penny.print_customers())
    penny.next_minute()
    print(penny.print_customers())
    penny.remove_existing_customers()
