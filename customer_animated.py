#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:46:09 2020

@author: hanbo
"""
import numpy as np
import time
import pandas as pd
#from transition_matrix import transition_matrix
transition_matrix = pd.read_csv("./data/transition_matrix.csv")
transition_matrix.set_index("location", inplace=True)
TILE_SIZE = 32
OFS = 50


class CustomerAnimated:
    ''' a single customer that moves through the supermarket in a MCMC simulation'''
    # constructor

    def __init__(self, terrain_map, image, x, y):

        self.terrain_map = 0
        self.image = 0
        self.x = 0
        self.y = 0

    # repr

    def __repr__(self):
        '''returns a csv string for that customer
        '''
        return f'{self.x}, {self.y}, {self.image}'

    def draw(self, frame):
        xpos = OFS + self.x * TILE_SIZE
        ypos = OFS + self.y * TILE_SIZE
        frame[ypos:ypos+32, xpos:xpos+32] = self.image
        # overlay the Customer image / sprite onto the frame


####customer journey simulation#####
# Driver function
# if __name__ == "__main__":
#     # spawn one customer
#     cust1 = Customer_animated(1, 'entrance', transition_matrix)

#      print(cust1.state)
#     print(cust1.path)
#     print(cust1)
