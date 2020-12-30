#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Customer class that simulates the paths
of new customers in the supermarket.
"""

import time

import numpy as np
import pandas as pd
import cv2

import astar as at
#from animation_template import SupermarketMap, MARKET


# from transition_matrix import transition_matrix
transition_matrix = pd.read_csv("./data/transition_matrix.csv")
transition_matrix.set_index("location", inplace=True)
tiles = cv2.imread('./images/tiles.png')

TILE_SIZE = 32
OFS = 50
# dest = pd.read_csv("./data/destinations.csv")
# dest.set_index("location", inplace=True)
dest = {
    "entrance_x": [9, 10],
    "entrance_y": [14],
    "dairy_x": [2, 4, 6],
    "dairy_y": [3],
    "fruit_x": [5, 6, 3],
    "fruit_y": [6],
    "spices_x": [6, 4, 2],
    "spices_y": [10],
    "drinks_x": [6, 4, 2],
    "drinks_y": [11],
    "checkout_x": [8, 9],
    "checkout_y": [7, 3]}


class Customer:
    ''' a single customer that moves through the supermarket in a MCMC simulation'''
    # constructor

    def __init__(self, id, state, transition_mat, terrain_map, image, x, y):
        self.id = id
        self.state = state
        self.transition_mat = transition_mat
        self.path = ["entrance"]
        self.terrain_map = terrain_map
        self.image = image
        self.x = x
        self.y = y
        self.path_to_dest = []

    # repr

    def __repr__(self):
        '''returns a csv string for that customer
        '''
        return f'{self.id}, {self.state}, {self.path}, {self.x},{self.y}'

    def is_active(self):
        '''
        Returns True if the customer has not reached the checkout for
        the second time yet, False otherwise.
        '''
        if self.state == 'checkout':
            return False
        else:
            return True

    # set state
    def next_state(self):
        '''Propagates the customer to the next state using a weighted
        random choice from the transition probabilites conditional on the
        current state.
        Returns nothing.
        '''
        # currently not using the transition probabilities
        next_location = np.random.choice(
            self.transition_mat.columns.values, p=self.transition_mat.loc[self.state])
        self.state = next_location
        self.path.append(self.state)

    def draw(self, frame):

        xpos = OFS + self.x * TILE_SIZE
        ypos = OFS + self.y * TILE_SIZE
        frame[ypos:ypos+self.image.shape[0],
              xpos:xpos + self.image.shape[0]] = self.image
        # overlay the Customer image / sprite onto the frame

    def get_shortest_path(self, grid, dest):
        start = self.path[len(self.path) - 2]
        end = self.state
        print(start)
        print(end)
        if start != end:
            start_loc_x = np.random.choice(dest[start+"_x"])
            start_loc_y = np.random.choice(dest[start+"_y"])
            end_loc_x = np.random.choice(dest[end+"_x"])
            end_loc_y = np.random.choice(dest[end + "_y"])
            print(start_loc_x)
            print(start_loc_y)
            print(end_loc_x)
            print(end_loc_y)

            path_to_dest = at.find_path(grid, (start_loc_x, start_loc_y),
                                        (end_loc_x, end_loc_y), at.possible_moves)[::-1]
            self.path_to_dest = path_to_dest

            print(self.path_to_dest)

    def to_move(self):
        if len(self.path_to_dest) > 0:
            return True

        return False

    def move(self):
        if len(self.path_to_dest) > 0:
            new_y, new_x = self.path_to_dest.pop()
            self.x = new_x
            self.y = new_y
            print(new_x, new_y)


# if __name__ == '__main__':
#     marketMap = SupermarketMap(MARKET, tiles)
#     cust1 = Customer(5, "entrance", transition_matrix, marketMap,
#                      tiles[3 * 32:4 * 32, 0 * 32:1 * 32], 15, 10)
#     cust1.next_state()
#     print(cust1)
#     cust1.get_shortest_path(grid=at.grid, dest=dest)
#     print(cust1.path_to_dest)
#     if cust1.path_to_dest != 0:
#         for next_p in cust1.path_to_dest:
#             cust1.move()
#             print(cust1)

#     print(cust1)
