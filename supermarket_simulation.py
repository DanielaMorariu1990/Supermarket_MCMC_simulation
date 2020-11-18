"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd
from datetime import datetime
from customer_simulation import Customer

transition_probabilities = pd.read_csv("data/transition_matrix.csv")
customer_path = pd.read_csv("data/customer_path.csv")


class Supermarket(Customer):
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self):
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
      #  self.last_id = 0
        self.possible_states = 5  # or list of locations?
        self.current_time = 0
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'Supermarket("{self.customers}", "{self.path}")'

    def get_time(self):
        """current time in HH:MM format,
        """
        # now = datetime.now().time() #creates a time object
        now = datetime.now()
        self.current_time = now.strftime("%H:%M")

    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        return f'Supermarket("{self.customers}", "{self.current_time}")'

    def next_minute(self):
        """propagates all customers to the next state.
        """
        self.current_time += datetime.timedelta(minutes=1)
        self.minutes += 1
        # we would need to call a next_state on customers
        for cust in self.customers:
            cust.state = cust.next_state()

    def add_new_customers(self, stop):
        """randomly creates new customers.
        """
        for i in range(stop):
            cust = Customer(i, "entrance", transition_probabilities)
            self.customers.append(cust)

    def remove_existing_customers():
        """removes every customer that is not active any more.
        """
        for cust in self.customers:
            if cust.is_active:
                pass

rewe = Supermarket()
rewe.print(customers)