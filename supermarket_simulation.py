"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd
from datetime import datetime
from customer_simulation import CustomerClass

transition_probabilities = pd.read_csv("data/transition_matrix.csv")
customer_path = pd.read_csv("data/customer_path.csv")

class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.possible_states = 5 #or list of locations?
        self.transition_probabilities = transition_probabilities
        self.path = customer_path

    def __repr__(self):
        return f'Supermarket("{self.customers}", "{self.path}")'

    def get_time():
        """current time in HH:MM format,
        """
        #now = datetime.now().time() #creates a time object
        now = datetime.now()
        current_time = now.strftime("%H:%M")


    def print_customers():
        """print all customers with the current time and id in CSV format.
        """
        return f'Supermarket("{self.customers}", "{self.current_time}")' #change to get_time


    def next_minute():
        """propagates all customers to the next state.
        """
    
    def add_new_customers():
        """randomly creates new customers.
        """
        for i in range(20):
            self.customers.append()

    def remove_exitsting_customers():
        """removes every customer that is not active any more.
        """