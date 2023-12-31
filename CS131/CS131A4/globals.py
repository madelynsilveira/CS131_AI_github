"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
CS131 - Artificial Intelligence

File to hold global variables, namely, the sudoku board.
by Madelyn Silveira
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

SIZE = 9
# DOMAIN = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# DOMAIN = [2, 3, 4, 5, 6, 7, 8, 9, 1]
# DOMAIN = [3, 4, 5, 6, 7, 8, 9, 1, 2]
# DOMAIN = [4, 5, 6, 7, 8, 9, 1, 2, 3]
# DOMAIN = [5, 6, 7, 8, 9, 1, 2, 3, 4]
# DOMAIN = [6, 7, 8, 9, 1, 2, 3, 4, 5]
# DOMAIN = [7, 8, 9, 1, 2, 3, 4, 5, 6]
# DOMAIN = [8, 9, 1, 2, 3, 4, 5, 6, 7]
DOMAIN = [9, 8, 7, 6, 5, 4, 3, 2, 1]

TEST1 = [
    [6, 0, 8, 7, 0, 2, 1, 0, 0],
    [4, 0, 0, 0, 1, 0, 0, 0, 2],
    [0, 2, 5, 4, 0, 0, 0, 0, 0],
    [7, 0, 1, 0, 8, 0, 4, 0, 5],
    [0, 8, 0, 0, 0, 0, 0, 7, 0],
    [5, 0, 9, 0, 6, 0, 3, 0, 1],
    [0, 0, 0, 0, 0, 6, 3, 0, 1],
    [2, 0, 0, 0, 9, 0, 0, 0, 8],
    [0, 0, 6, 8, 0, 5, 2, 0, 3]
]

TEST2 = [
    [0, 7, 0, 0, 4, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 6, 1, 0],
    [3, 9, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 4, 0, 0, 9],
    [0, 0, 3, 0, 0, 0, 7, 0, 0],
    [5, 0, 0, 1, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 7, 6],
    [0, 5, 4, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 1, 0, 0, 5, 0]
]

TEST3 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

TEST4 = [
[0, 6, 0, 1, 0, 4, 0, 5, 0],
[0, 0, 8, 3, 0, 5, 6, 0, 0],
[2, 0, 0, 0, 0, 0, 0, 0, 1],
[8, 0, 0, 4, 0, 7, 0, 0, 6],
[0, 0, 6, 0, 0, 0, 3, 0, 0],
[7, 0, 0, 9, 0, 1, 0, 0, 4],
[5, 0, 0, 0, 0, 0, 0, 0, 2],
[0, 0, 7, 2, 0, 6, 9, 0, 0],
[0, 4, 0, 5, 0, 8, 0, 7, 0]
]

TEST5 = [
[0, 0, 0, 0, 0, 0, 1, 9, 0],
[0, 0, 0, 0, 0, 8, 0, 0, 0],
[0, 3, 0, 0, 0, 0, 7, 0, 0],
[0, 2, 0, 0, 0, 6, 0, 0, 9],
[0, 0, 0, 2, 3, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 6, 0],
[9, 0, 0, 0, 0, 0, 0, 0, 0],
[2, 0, 4, 0, 0, 0, 0, 5, 0],
[0, 0, 3, 0, 5, 0, 0, 0, 0]
]

EMPTY = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

FULL = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]