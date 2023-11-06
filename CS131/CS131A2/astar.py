#
# CS131 - Artificial Intelligence
#
# Implementation of the A* Algorithm for the pancake problem with 10 pancakes.
# Uses a Priority Queue where the priority is h(n) + g(n)
# by Madelyn Silveira
# 

from queue import PriorityQueue
from pancakes import flip

def astar(stack):
    """
    Implements the A* algorithm. Path = indices to be flipped, in order.
    """
    # instantiate variables
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    frontier = PriorityQueue()
    frontier.put((heuristic(stack), stack, [])) # priority, current stack, path to get there
    seen = []

    # keep going until you've found a stack that matches the goal
    while not frontier.empty():
        # get the element of lowest priority
        priority, current, path = frontier.get()

        # check if this stack is sorted
        if current == goal:
            return path, len(path)

        # add all possible flips to the frontier
        for i in range(1, 10):
            # flip the pancakes up until ith index
            flipped = flip(current, i)
            if flipped not in seen:
                priority = cost(i) + heuristic(flipped)
                frontier.put((priority, flipped, path + [i]))
                seen.append(flipped)
        
        
    return [], 0


def heuristic(stack):
    """
    Calculates the number of pancakes out of position in current stack.
    """
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    toMove = 0

    for i in range(0, 10):
        if stack[i] != goal[i]:
            toMove += 1
    return toMove

def cost(path):
    """
    Calculates the number of pancakes being flipped. Path is the index of 
    the pancake being flipped.
    """
    return path 
