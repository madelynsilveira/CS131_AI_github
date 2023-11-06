#
# CS131 - Artificial Intelligence
#
# Implementation of th A* Algorithm.
# Uses a Priority Queue where the priority is h(n) + g(n)
# by Madelyn Silveira
# 

import sys
from pancakes import printCakes, flip
from astar import astar, heuristic, cost

# Instantiate an array of pancakes
cakes = [10, 9, 8, 5, 1, 4, 3, 2, 7, 6]
# cakes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call astar algorithm
# print("initial stack: " + str(cakes))

path, cost = astar(cakes)

# print("final stack: " + str(cakes))
# print("path: " + str(path))
# print("cost: " + str(cost))

# Output data in fun way





