"""
Start with this to implement the supermarket simulator.
"""

import time
import datetime

import numpy as np
import pandas as pd
import cv2

import astar as at
from customer_simulation import Customer, dest
from animation_template import SupermarketMap, MARKET

transition_matrix = pd.read_csv("data/transition_matrix.csv")
transition_matrix.set_index("location", inplace=True)

tiles = cv2.imread('./images/tiles.png')
# dest = pd.read_csv("./data/destinations.csv")
# dest.set_index("location", inplace=True)


class Supermarket():
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self, market):
        # a list of Customer objects
        self.customers = []  # here we need the Customer class!
        self.minutes = 0  # how many minutes have passed?
        self.id_suffix = 0  # we can concatenate it with the id from customer
        self.possible_states = 5  # or list of locations?
        self.market = market  # current supermarket time
        self.current_time = 0
        self.to_move = False

    def __repr__(self):
        # should return :
        # - customers, state (path) of customers,current time, time elapsed
        return f'Supermarket("{self.customers}", "{self.current_time}")'

    def get_time(self):
        """current time in HH:MM format,
        """
        # now = datetime.now().time() #creates a time object
        hour = self.minutes // 60 + 7
        minutes = self.minutes % 60
        return f'{str(hour).zfill(2)}:{str(minutes).zfill(2)}'

    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        # current time --> supermarket
        # customer.state --> from customers
        # customer.id --> Customer
        self.current_time = self.get_time()
        return f'Supermarket("{self.customers}", "{self.current_time}")'

    def next_minute(self):
        """propagates all customers to the next state.
        """

        self.minutes += 1
        # we would need to call a next_state on customers
        # I do not know how to access it to print it????
        for cust in self.customers:
            cust.next_state()
            cust.get_shortest_path(grid=at.grid, dest=dest)

        self.to_move = True

    def move_customers(self):
        for cust in self.customers:
            cust.move()

    def draw_customers(self, frame):
        '''
        draw all the customers
        '''
        for customer in self.customers:
            customer.draw(frame)

    def add_new_customers(self, stop, id_suffix, terrain_map, image, x, y):
        """randomly creates new customers.
        """
        for i in range(stop):
            cust = Customer(str(i) + "_" + str(id_suffix), "entrance", transition_matrix,
                            terrain_map=terrain_map, image=image, x=x, y=y)
            self.customers.append(cust)

        self.id_suffix += 1

    def remove_existing_customers(self):
        """removes every customer that is not active any more.
        """
        # remove the customers which are not active (.is_active )
        self.to_move = False
        for cust in self.customers:
            if cust.state == 'checkout':
                self.customers.remove(cust)
                print(f'{cust} removed')

            if cust.to_move():
                self.to_move = True
