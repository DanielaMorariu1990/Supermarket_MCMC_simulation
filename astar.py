"""
A* algorithm
"""
import operator
import numpy as np
from animation_template import MARKET
import pandas as pd


def heuristic(current, target):
    """calculating the estimated distance between the current node and the targeted node
       -> Manhattan Distance"""

    result = (abs(target[0] - current[0]) + abs(target[1] - current[1]))
    # print(result)
    return result


def walkable(grid_array): 
    """checks if node is on the grid and not an obstacle"""

    obstacles = [entrance, drinks, dairy, spices, fruit, checkout]
    walkable = []

    for i in range(len(grid_array)):
        for j in range(len(grid_array[0])):
            if grid_array[i, j] == 0:
                walkable.append((i, j))
               # print(walkable)
    return walkable


def get_path_from_finish(current):
    """Traces back the path thourgh parent-nodes"""

    backwards = []
    while current:
        backwards.append(current.location)
        current = current.parent
    backwards.reverse()
    return backwards


def create_neighbours(poss_moves, current_node, finish_node, grid_array, frontier):
    """Creates neighbour-nodes for current node and adds them to the frontier-list"""

    for move in poss_moves:
        node_position = (current_node.location[0] + move[0],
                         current_node.location[1] + move[1])
        if node_position in walkable(grid_array):
            neighbour = Node(parent=current_node,
                             location=node_position,
                             cost=current_node.cost + 1,
                             heur=heuristic(node_position, finish_node.location))
           # print(neighbour)
            frontier.append(neighbour)
    return frontier


def find_path(grid_array, start, finish, p_moves):
    """ A*-Algorithm that finds the shortest path between
        given nodes and returns it as list of tuples"""

    start_node = Node(None, start)
    finish_node = Node(None, finish)
    frontier = [start_node]

    while frontier:
        frontier.sort(key=operator.attrgetter('f_value'))
        current_node = frontier[0]
        frontier.pop(0)

        if current_node.location != finish_node.location:
            frontier = create_neighbours(
                p_moves, current_node, finish_node, grid_array, frontier)
            # print(frontier)
        else:
            shortest_path = get_path_from_finish(current_node)
            return shortest_path


class Node():
    """Class for the nodes of a pathfinding grid"""

    def __init__(self, parent, location, cost=0, heur=0):
        self.parent = parent
        self.location = location
        self.cost = cost  # distance from start-node (cost)
        self.heur = heur  # approx. distance to goal-node
        self.f_value = self.cost + self.heur  # sum of cost and heuristic value


grid = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
])


possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

if __name__ == '__main__':
    grid = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ])

    # wakable = grid[1, 2:16]
    # wakable = wakable.append(grid[3:11, 2:4])
    # wakable = wakable.append(grid[3:11, 6:8])

    # walk = walkable(grid)
    # print(walk)
    # pd.DataFrame(walk).to_csv("./data/walk.csv")

    # # y,x positions
    # start_given = (1, 0)
    # finish_given = (2, 5)
    # possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0),
    #                   (1, 1), (1, -1), (-1, 1), (-1, -1)]
    # path = find_path(grid, start_given, finish_given, possible_moves)
    # print(path)

    # strat = x, y from Customer
    # finish_given= transition_matrix.loc[]
    # for the path function:
    # - grid =market

   # grid = MARKET
    # print(MARKET)
    entrance = (15, 10)
    dairy = (5, 2)
    fruits = (6, 5)
    spices = (9, 6)
    drinks = (4, 6)
    checkout = (9, 8)
    possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
    path = find_path(grid, (10+1, 15+1), (2+1, 5+1), possible_moves)
    print(path)
