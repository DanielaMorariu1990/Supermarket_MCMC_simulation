#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:46:09 2020

@author: hanbo
"""
import numpy as np
import time
import pandas as pd
# from transition_matrix import transition_matrix
transition_matrix = pd.read_csv("./data/transition_matrix.csv")
transition_matrix.set_index("location", inplace=True)


class Customer:
    ''' a single customer that moves through the supermarket in a MCMC simulation'''
    # constructor

    def __init__(self, id, state, transition_mat):
        self.id = id
        self.state = state
        self.transition_mat = transition_mat
        self.path = []]

    # repr
    def __repr__(self):
        '''returns a csv string for that customer
        '''
        return f'Customer {self.id}, in {self.state}'

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
            self.transition_mat.columns.values, p = self.transition_mat.loc[self.state])
        self.state=next_location


####customer journey simulation#####
if __name__ == "__main__":

    # single customer simulation
    cust1=Customer(1, 'entrance', transition_matrix)

    # check state of customer, if 'checkout' delete the customer
    while cust1.state != 'checkout':
        cust1.next_state()
        print(cust1)
        # for testing purposes set time to one second
        # for implementation set to one minute
        time.sleep(1)

    # serial multiple customer simulation
    my_customers={}
    for i in range(5):
        my_cust=Customer(i, 'entrance', transition_matrix)
        my_customers[i]=my_cust

    my_customers[0].is_active()
    # how do I get them all to change state simultaneously?
    for cust in my_customers:
        while my_customers[cust].is_active():
            my_customers[cust].next_state()
            print(my_customers[cust])
            time.sleep(1)

    # how to implement simultaneous simulation?
