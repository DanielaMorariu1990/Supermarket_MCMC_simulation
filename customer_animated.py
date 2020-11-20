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

        self.terrain_map = terrain_map
        self.image = image
        self.x = x
        self.y = y

    # repr

    def __repr__(self):
        '''returns a csv string for that customer
        '''
        return f'{self.x}, {self.y}, {self.image}'

    def draw(self, frame):
        xpos = OFS + self.x * TILE_SIZE
        ypos = OFS + self.y * TILE_SIZE
        frame[ypos:ypos+self.image.shape[0],
              xpos:xpos + self.image.shape[0]] = self.image
        # overlay the Customer image / sprite onto the frame

    def move(self, direction):
        newx = self.x
        newy = self.y
        if direction == 'up':
            newy -= 1

        if self.terrain_map.contents[newy][newx] == '.':
            self.x = newx
            self.y = newy


####customer journey simulation#####
# Driver function
# if __name__ == "__main__":
#     # spawn one customer
#     cust1 = Customer_animated(1, 'entrance', transition_matrix)

#      print(cust1.state)
#     print(cust1.path)
#     print(cust1)
