#
# CS131 - Artificial Intelligence
#
# Pancakes functions
# by Madelyn Silveira
# 

import sys

def printCakes(cakes):
    for i in range(10):
        if cakes[i] == 10: sys.stdout.write(str(cakes[i])+ ": ")
        else: sys.stdout.write(str(cakes[i])+ ":  ")
        while cakes[i] != 0:
            sys.stdout.write('---')
            cakes[i] = cakes[i] - 1
        sys.stdout.write('\n')

# cakes = [1, 2, 3, 4,        5, 6, 7, 8, 9, 10]
# result = [4, 3, 2, 1,       5, 6, 7, 8, 9, 10]


# stack = [1, 2, 3, 4,            5, 6, 7, 8, 9, 10]
# stack = [10, 9, 8, 7, 6, 5,     4, 3, 2, 1]


def flip(stack, index):
    new = stack
    reversed = stack[:]
    reversed = reversed[::-1]
    count = 0
    for i in range(9 - index, 10):
        new[count] = reversed[i]
        count += 1
    return new


L=[1,2,3]
# R=L
R = L[:]
L.reverse()
