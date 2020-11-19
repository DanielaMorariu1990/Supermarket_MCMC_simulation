"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd
import datetime
import cv2
from customer_simulation import Customer
from animation_template import SupermarketMap, MARKET
import time

transition_matrix = pd.read_csv("data/transition_matrix.csv")
transition_matrix.set_index("location", inplace=True)

tiles = cv2.imread('./images/tiles.png')


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
            cust.move("up")

    def add_new_customers(self, stop, terrain_map, image, x, y):
        """randomly creates new customers.
        """
        for i in range(stop):
            cust = Customer(i, "entrance", transition_matrix,
                            terrain_map=terrain_map, image=image, x=x, y=y)
            self.customers.append(cust)

    def remove_existing_customers(self):
        """removes every customer that is not active any more.
        """
        # remove the customers which are not active (.is_active )

        for cust in self.customers:
            if cust.state == 'checkout':
                self.customers.remove(cust)
                print(f'{cust } removed')


# we need to hardcode coordinates of location
entrance = (15, 10)
dairy = (5, 2)
fruits = (6, 5)
spices = (9, 6)
drinks = (4, 6)
checkout = (9, 8)

if __name__ == '__main__':
    background = np.zeros((700, 1000, 3), np.uint8)
    penny = Supermarket()
    marketMap = SupermarketMap(MARKET, tiles)
    penny.get_time()
    penny.add_new_customers(1, marketMap,
                            tiles[3 * 32:4 * 32, 0 * 32:1 * 32], entrance[0], entrance[1])

    while True:
        frame = background.copy()
        marketMap.draw(frame)

        time.sleep(5)
       # penny.next_minute()
        print(penny.print_customers())
        # we need to iterate in oredr to call .move()
        penny.customers[0].draw(frame)
        print(penny.print_customers())
        cv2.imshow('frame', frame)

        key = chr(cv2.waitKey(1) & 0xFF)
        if key == 'q':
            break

    # time.sleep(1)

    # print(penny.print_customers())
    # penny.customers[0].move(direction='up')
    # print(penny.print_customers())
    # time.sleep(1)
    # penny.next_minute()
    # print(penny.print_customers())
    # penny.next_minute()
    # print(penny.print_customers())
    # penny.remove_existing_customers()
