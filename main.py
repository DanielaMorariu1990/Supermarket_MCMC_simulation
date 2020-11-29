import time
import datetime

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


if __name__ == '__main__':
    background = np.zeros((700, 1000, 3), np.uint8)
    penny = Supermarket()
    marketMap = SupermarketMap(MARKET, tiles)
    penny.get_time()
    penny.add_new_customers(1, 0, marketMap,
                            ghost, entrance[0], entrance[1])
    my_suffix = 1
    while True:

        frame = background.copy()
        marketMap.draw(frame)

        for i in range(len(penny.customers)):
            penny.customers[i].draw(frame)
            print(penny.customers[i])

        time.sleep(2)

        penny.next_minute()
        print(penny.print_customers())

        # we need to iterate in oredr to call .move()

        penny.remove_existing_customers()
        # penny.add_new_customers(1, my_suffix, marketMap,
        #                         pacman, entrance[0], entrance[1])

        # penny.add_new_customers(1, my_suffix, marketMap,
        #                         ghost, entrance[0], entrance[1])
        # my_suffix += 1

        print(penny.print_customers())
        cv2.imshow('frame', frame)

        key = chr(cv2.waitKey(1) & 0xFF)
        if key == 'q':
            break
