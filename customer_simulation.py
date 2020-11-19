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


class Customer:
    ''' a single customer that moves through the supermarket in a MCMC simulation'''
    # constructor

    def __init__(self, id, state, transition_mat):
        self.id = id
        self.state = state
        self.transition_mat = transition_mat
        self.path = []

    # repr

    def __repr__(self):
        '''returns a csv string for that customer
        '''
        return f'{self.id}, {self.state}, {self.path}'

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


####customer journey simulation#####
# Driver function
if __name__ == "__main__":
    # spawn one customer
    cust1 = Customer(1, 'entrance', transition_matrix)

    # check state of customer, if 'checkout' delete the customer
    while cust1.state != 'checkout':
        cust1.next_state()
        # for testing purposes set time to one second
        # for implementation set to one minute
        time.sleep(1)

    print(cust1.state)
    print(cust1.path)
    print(cust1)
