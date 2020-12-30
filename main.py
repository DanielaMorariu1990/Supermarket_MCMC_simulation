import time
import datetime
from random import random

import numpy as np
import pandas as pd
import cv2

from supermarket_simulation import Supermarket
from customer_simulation import Customer, dest
from animation_template import SupermarketMap, MARKET
import astar as at


transition_matrix = pd.read_csv("data/transition_matrix.csv")
transition_matrix.set_index("location", inplace=True)

tiles = cv2.imread('./images/tiles.png')

# we need to hardcode coordinates of location
entrance = (15, 10)
dairy = (5, 2)
fruits = (6, 5)
spices = (9, 6)
drinks = (4, 6)
checkout = (9, 8)
pacman = tiles[3 * 32:4 * 32, 0 * 32:1 * 32]
pacman2 = tiles[3 * 32:4 * 32, 1 * 32:2 * 32]
ghost = tiles[7 * 32:8 * 32, 1 * 32:2 * 32]


def move_between_minutes(market, supermarket, frame):
    ''' move the customers between the minutes'''
    market.draw(frame)
    supermarket.remove_existing_customers()
    supermarket.move_customers()
    supermarket.print_customers()
    supermarket.draw_customers(frame)
    time.sleep(0.1)


def go_to_next_minute(market, supermarket, frame, adding_prob=0):
    '''
    simulate next minute
    '''
    market.draw(frame)
    if random() < adding_prob:
        supermarket.add_new_customers()
    supermarket.remove_existing_customers()
    supermarket.print_customers()

    supermarket.draw_customers(frame)
    supermarket.next_minute()
    time.sleep(0.1)
    return supermarket


def simulate_n_customers(n, ghost, transition_matrix):
    '''
    Simulate n customers that start together in the store.
    No new customers are added over time.
    The simulation ends once all are checked out.
    '''
    background = np.zeros((700, 1000, 3), np.uint8)
    market = SupermarketMap(MARKET, tiles)
    supermarket = Supermarket(market=market)
    id_suffix = 0
    for _ in range(n):
        supermarket.add_new_customers(
            stop=1, id_suffix=id_suffix,  terrain_map=market, image=ghost, x=entrance[0], y=entrance[1])
    frame = background.copy()

    while len(supermarket.customers) > 0:
        if supermarket.to_move:
            move_between_minutes(market, supermarket, frame)
        else:
            go_to_next_minute(market, supermarket, frame)
        cv2.imshow("frame", frame)

        key = chr(cv2.waitKey(1) & 0xFF)
        if key == 'q':
            break
    cv2.destroyAllWindows()
    market.write_image("./graphics/supermarket.png")
    id_suffix += 1


simulate_n_customers(n=10, ghost=ghost, transition_matrix=transition_matrix)
