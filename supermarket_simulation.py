"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd


class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self):        
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0

    def __repr__(self):
        pass

    def get_time():
        """current time in HH:MM format,
        """

    def print_customers():
        """print all customers with the current time and id in CSV format.
        """

    def next_minute():
        """propagates all customers to the next state.
        """
    
    def add_new_customers():
        """randomly creates new customers.
        """

    def remove_exitsting_customers():
        """removes every customer that is not active any more.
        """