"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
CS131 - Artificial Intelligence

Implementation of a Sudoku Solver that solves a sudoku board using a
Constraint Satisfaction approach.

by Madelyn Silveira
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import collections
from globals import SIZE, DOMAIN


def printBoard(board):
    """
    Prints a Sudoku board and tells if the board is a valid solution or not.
    """
    for i in range(SIZE):
        
        # print a horizontal line every three rows
        if i % 3 == 0:
            print("-" * 25)
        
        # print values in each row
        for j in range(SIZE):

            # print dividers
            if j % 3 == 0:
                print("| ", end="")

            print(board[i][j], end=" ")

        print("|")
    
    # ending line
    print("-" * 25)
    print("\nBoard Passes: " + str(checkBoard(board)) + "\n")


"""------------------------Testing Solutions------------------------"""

def checkBoard(board):
    """
    Checks to see if a board is a legitimate sudoku solution.
    """
    for i in range(SIZE):
        if (not checkRow(board[i])): return False
        if (not checkCol(board, i)): return False
    
    corners = [0, 0, 0, 3, 0, 6, 3, 0, 3, 3, 3, 6, 6, 0, 6, 3, 6, 6]
    for i in range(3):
        if (not checkSquare(board, int(corners.pop()), int(corners.pop()))): 
            return False
    
    return True
    

def checkRow(row):
    """
    Checks to see if a given row includes all elements exactly once.
    """
    elements = []

    for i in range(SIZE):
        elements.append(row[i])

    if collections.Counter(elements) == collections.Counter(DOMAIN):
        return True
    
    return False

def checkCol(board, col):
    """
    Checks to see if a given column includes all elements exactly once.
    """
    elements = []

    for i in range(SIZE):
        elements.append(board[col][i])

    if collections.Counter(elements) == collections.Counter(DOMAIN):
        return True
    
    return False

def checkSquare(board, row, col):
    """
    Checks to see if a given 3x3 square includes all elements exactly once.
    """
    elements = []

    for row in range(3):
        for col in range(3):
            elements.append(board[row][col])

    if collections.Counter(elements) == collections.Counter(DOMAIN):
        return True
    
    return False


