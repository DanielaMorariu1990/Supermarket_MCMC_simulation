"""
Calculate transition matrix for each section
in the supermarket
"""

import pandas as pd
import numpy as np

# correct data (customers with no marked checkout)


def missing_checkout(data):
    checkout = set(data[data["location"] == "checkout"]
                   ["customer_no"].unique())
    all_c = set(data["customer_no"].unique())
    diff = all_c.difference(checkout)
    for cust in diff:
        data = data.append({"timestamp": "2019-09-02 22:00:00", "customer_no": cust,
                            "location": "checkout"}, ignore_index=True)

    return data

# make customer name unique


def cust_no_name(data, weekday):
    data["customer_no"] = data["customer_no"].apply(
        lambda x: str(x)+"_" + weekday)
    return data


##read in data
monday = pd.read_csv("./data/monday.csv", header=0, sep=";", parse_dates=True)
missing_checkout(monday)
monday["weekday"] = "monday"
cust_no_name(monday, "monday")

tuesday = pd.read_csv("./data/tuesday.csv", header=0,
                      sep=";", parse_dates=True)
missing_checkout(tuesday)
tuesday["weekday"] = "tuesday"
cust_no_name(tuesday, "tuesday")

wednesday = pd.read_csv("./data/wednesday.csv",
                        header=0, sep=";", parse_dates=True)
missing_checkout(wednesday)
wednesday["weekday"] = "wednesday"
cust_no_name(wednesday, "wednesday")

thursday = pd.read_csv("./data/thursday.csv", header=0,
                       sep=";", parse_dates=True)
missing_checkout(thursday)
thursday["weekday"] = "thursday"
cust_no_name(thursday, "thursday")

friday = pd.read_csv("./data/thursday.csv", header=0,
                     sep=";", parse_dates=True)
missing_checkout(friday)
friday["weekday"] = "friday"
cust_no_name(friday, "friday")

# concatenate each weekday in one data frame
data = pd.concat([monday, tuesday, wednesday, thursday, friday])

# values need to be sorted inplace, such that we have
# correct transitions
# calculate next location (transition from one section to the other)
data.sort_values(["customer_no", "timestamp"], inplace=True)

data["location_next"] = data["location"].shift(-1)

# checkout will only migrate to checkout!
data.loc[(data.location == 'checkout'), 'location_next'] = 'checkout'

# collect the final states
states = data[["location", "location_next"]]

# calculate transition matrix
transition_matrix = pd.crosstab(
    data['location'], data['location_next'], normalize=0)

# check if the matrix is correct
transition_matrix.sum(axis=1)

# export the transition prob matrix to csv
transition_matrix.to_csv("./data/transition_matrix.csv")