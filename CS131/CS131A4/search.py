"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
CS131 - Artificial Intelligence

Implementation of a Sudoku Solver that solves a sudoku board using a
Constraint Satisfaction approach.

by Madelyn Silveira
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from globals import SIZE, DOMAIN
from sudoku import printBoard

def run(board):
    """
    Calls the searching algorithm and prints relevant information.
    """
    print("\nInitial Board")
    printBoard(board)
    if solve(board):
        print("\nFinal Board")
        printBoard(board)
    else:
        printBoard(board)
        print("No solution found. Check input board.\n")

def solve(board):
    """
    Implementation of backtracking search algorithm to solve sudoku board.
    """

    # Find an empty cell
    row, col = emptyCell(board)

    if row == -1 or col == -1:
        return True

    # try out potential elements
    elements = forwardCheck(board, row, col)

    for i in range(len(elements)):

        board[row][col] = elements[i]

        # recursive call to work on next solution
        if solve(board):
            return True
        
        # reset for backtracking purposes
        board[row][col] = 0

    return False


def emptyCell(board):
    """
    Finds the next empty cell for variable assignment.
    """
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0:
                return i, j

    return -1, -1

def forwardCheck(board, row, col):
    """
    Creates and returns a list of elements available for a given index.
    """
    elements = DOMAIN.copy()

    for i in range(SIZE):
        if board[row][i] in elements: elements.remove(board[row][i])
        if board[i][col] in elements: elements.remove(board[i][col])

    # check the 3x3 square for this index
    sqRow = (row//3)*3
    sqCol = (col//3)*3

    for i in range(3):
        for j in range(3):
            if board[sqRow + i][sqCol + j] in elements: 
                elements.remove(board[sqRow + i][sqCol + j])
   
    return elements



