import numpy as np
import time

grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def possible(y, x, n) :
    global grid
    for i in range(0, 9) :
        if grid[y][i] == n :
            return False
    for i in range(0, 9) :
        if grid[i][x] == n :
            return False
    x_square = (x//3) * 3
    y_square = (y//3) * 3
    for i in range(0, 3) :
        for j in range(0, 3) :
            if grid[y_square+i][x_square+j] == n :
                return False
    return True

def print_and_clear() :
    print(chr(27) + "[2J")
    print(np.matrix(grid))
    time.sleep(0.05)

def solver() :
    global grid
    for y in range(9) :
        for x in range(9):
            if grid[y][x] == 0 :
                for n in range(1, 10) :
                    if possible(y,x,n) == True :
                        grid[y][x] = n
                        solver()
                        grid[y][x] = 0
                        #print_and_clear()
                return
    print(np.matrix(grid))

def main() :
    global grid
    print("Initial sudoku :")
    print(np.matrix(grid), "\n")
    print("Solution :")
    solver()

main()
