#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:46:09 2020

@author: hanbo
"""
import numpy as np
import time
import pandas as pd
import astar as at
from animation_template import SupermarketMap, MARKET
import time
import cv2
from animation_template import MARKET


# from transition_matrix import transition_matrix
transition_matrix = pd.read_csv("./data/transition_matrix.csv")
transition_matrix.set_index("location", inplace=True)
tiles = cv2.imread('./images/tiles.png')

TILE_SIZE = 32
OFS = 50
dest = pd.read_csv("./data/destinations.csv")
dest.set_index("location", inplace=True)


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
        self.path_to_dest = 0

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
        start_loc_x = dest.loc[start]["x"] + 1
        start_loc_y = dest.loc[start]["y"]+1
        end_loc_x = dest.loc[end]["x"] + 1
        end_loc_y = dest.loc[end]["y"] + 1

        path_to_dest = at.find_path(grid, (start_loc_x, start_loc_y),
                                    (end_loc_x, end_loc_y), at.possible_moves)
        self.path_to_dest = path_to_dest
        print(self.path_to_dest)

    def move(self, next_p):
        if next_p is not None:
            self.x = next_p[0]
            self.y = next_p[1]


marketMap = SupermarketMap(MARKET, tiles)
cust1 = Customer(1, "entrance", transition_matrix, marketMap,
                 tiles[3 * 32:4 * 32, 0 * 32:1 * 32], 15, 10)
cust1.next_state()
cust1.get_shortest_path(grid=at.grid, dest=dest)
for next_p in cust1.path_to_dest:
    print(next_p)

print(cust1)
# ####customer journey simulation#####
# # Driver function
# if __name__ == "__main__":
#     # spawn one customer
#     cust1 = Customer(1, 'entrance', transition_matrix)

#     # check state of customer, if 'checkout' delete the customer
#     while cust1.state != 'checkout':
#         cust1.next_state()
#         # for testing purposes set time to one second
#         # for implementation set to one minute
#         time.sleep(1)

#     print(cust1.state)
#     print(cust1.path)
#     print(cust1)
