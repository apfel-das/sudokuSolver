


# solver.py

"""
Actual Sudoku Solver 
Input: The board as a 2d list, dimensions as int
Return: True (if solved) or False (not solved)

"""

def solve(bo, dim):
   
    
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,dim):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo, dim):
                return True

            bo[row][col] = 0

    return False


"""
    Returns if the attempted move is valid
    :bo: 2d list of ints
    :pos: a set of (row, col) int the list
    :num: int
    :return: True or False
    """


def valid(bo, pos, num):
    

    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

"""
    
Locates any empty space int the given (2d list ) board
Returns: a set of (i,j) coordinates or None    


"""


def find_empty(bo):
    

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None

"""
Prints any given board (should be a 2d list) in a more graphic way
Returns: Nothing

"""


def print_board(bo):
   
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("--------------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                if bo[i][j] != 0:
                    print(bo[i][j], end="\n")
                else:
                     print("x", end="\n")
            else:
                if bo[i][j] != 0:
                    print(str(bo[i][j]), end=" ")
                else:
                     print("x", end=" ")





# Driver main function to test above functions 
if __name__=="__main__": 
      
    print("Test!");  

    # creating a 2D array for the grid 
    grid=[[0 for x in range(9)]for y in range(9)] 

      
    # assigning values to the grid 
    grid=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]] 
    print_board(grid)      

    solve(grid, 10)
    if solve(grid, 10):
        print("Solved!")
        print_board(grid)
