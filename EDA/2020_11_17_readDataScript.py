#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:49:50 2020

Script for iterating over data csv files in a data directory, and saving them in a dictionary of pandas dataframes

@author: hanbo
"""

import os
from pathlib import Path
import pandas as pd

####################################

data_dir= '../data'
files = os.listdir(data_dir)
my_sep = ';'
my_dfs = {}

for file in files:
    
   full_path = Path(data_dir) / Path(file)
   #print(full_path)
   #add each df to a dictionary
   df_name = file.split('.')[0]
   #print(df_name)
   df = pd.read_csv(full_path, sep = my_sep)
   my_dfs[df_name] = df