def grid_intro():
    sudoku_grid=[[-1, -1, -1, 2, 6, -1, 7, -1, 1],
                             [6, 8, -1, -1, 7, -1, -1, 9, -1],
                             [1, 9, -1, -1, -1, 4, 5, -1, -1],
                             [8, 2, -1, 1, -1, -1, -1, 4, -1],
                             [-1, -1, 4, 6, -1, 2, 9, -1, -1],
                             [-1, 5, -1, -1,-1, 3, -1, 2, 8],
                             [-1, -1, 9, 3, -1, -1, -1, 7, 4],
                             [-1, 4, -1, -1, 5, -1, -1, 3, 6],
                             [7, -1, 3, -1, 1, 8, -1, -1, -1]]
    
    modify_sud=sudoku_grid
    guess= [1, 2, 3, 4, 5, 6, 7, 8, 9]
    solve_sudoku(sudoku_grid, modify_sud, guess)                                                

def check_is_free(sud):
    for row in range(9):
        for col in range(9):
            if sud[row][col]==-1:
                return row, col
                print(row, col)
                print("hey")
    return None, None  

def is_valid(num, row, col, b):
            if num in b[row] or num in b[col]:
                return False
            else:
                return True                                
            
def solve_sudoku(a, b, guess):
    row, col=check_is_free(b)
    if is_valid(guess[-1], row, col, b):
                b[row][col]=guess[-1]
                last=b[row][col]
                solve_sudoku()
                
    else:
                guess.pop()
                solve_sudoku()            
    if not(guess):
                    
    if check_is_free(b) == None and None:
        print(b)                  
        exit()
grid_intro()                                                                        