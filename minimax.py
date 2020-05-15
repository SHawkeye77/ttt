"""
Samuel Hohenshell
File contains functions for the minimax AI implementation for tic-tac-toe
"""

import ttt


# Returns False if board is full, True otherwise
def moves_left(grid):
    for r in range(0,3):
        for c in range(0,3):
            if grid[r][c] == '_':
                return True
    return False


# Evaluation function (minimax) for tic-tac-toe game for the current state
# of the board. Returns 10 if user won, -10 if AI won, and 0 if neither won.
def evaluate(grid, pl_el, ai_el):
    # Checks ROWS for a win
    for r in range(0, 3): 
        if grid[r][0] == grid[r][1] and grid[r][1] == grid[r][2]:
            if grid[r][0] == pl_el:    # Player won, return 10
                return 10 
            elif grid[r][0] == ai_el:  # AI won, return -10
                return -10 
    # Checks COLUMNS for a win 
    for c in range(0, 3):
        if grid[0][c] == grid[1][c] and grid[1][c] == grid[2][c]:  
            if grid[0][c] == pl_el:    # Player won, return 10
                return 10 
            elif grid[0][c] == ai_el:  # AI won, return -10
                return -10 
    # Checks DIAGONALS for a win 
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:  
        if grid[0][0] == pl_el:    # Player won, return 10
            return 10 
        elif grid[0][0] == ai_el:  # AI won, return -10
            return -10 
    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:  
        if grid[0][2] == pl_el:    # Player won, return 10
            return 10 
        elif grid[0][2] == ai_el:  # AI won, return -10
            return -10 
    # If nobody has won, return zero 
    return 0 
   

# Returns overall minimax value of the current board
def minimax(grid, depth, max_turn, pl_el, ai_el):
    cur_score = evaluate(grid, pl_el, ai_el)  # Score on the exact, current state of board (no recursive calls)

    # Return score if game is complete (player/AI won or tie)
    if cur_score == 10:           # Player won
        return cur_score
    elif cur_score == -10:        # AI won
        return cur_score
    else:
        if not moves_left(grid):  # Tie
            return 0

    # If it's max's (Human's) turn (wants largest value)
    if max_turn:
        best = -1000  # Starting "best" at a value that will be overwritten
        # Traversing all cells, making all moves using a backtracking algorithm
        for r in range(0, 3):
            for c in range(0, 3):
                # If cell is empty
                if grid[r][c] == '_':
                    # Make move
                    grid[r][c] = pl_el
                    # Check how this changes outcome
                    best = max(best, minimax(grid, depth+1, not max_turn, pl_el, ai_el))
                    # Undo move
                    grid[r][c] = '_'
        return best  # Returns best possible value aka the minimax value

    # If it's min's (AI's) turn (wants smallest value)
    else:
        best = 1000  # Starting best at a value that will be overwritten
        # Traversing all cells, making all moves using a backtracking algorithm
        for r in range(0, 3):
            for c in range(0, 3):
                # If cell is empty
                if (grid[r][c] == '_'):
                    # Make move
                    grid[r][c] = ai_el
                    # Check how this changes outcome
                    best = min(best, minimax(grid, depth+1, not max_turn, pl_el, ai_el))
                    # Undo move
                    grid[r][c] = '_'
        return best  # Returns best possible value aka the minimax value


# Returns best possible move in form (row, column)
# Only gets called once and is only called when it is the AI's move
def get_best_move(grid, pl_el, ai_el):
    best_val = 1000       # AI wants smallest value, this will be overwritten
    best_move = (-1, -1)  # Will store the best move
    # Evaluate minimax for all empty cells, return cell with optimal value
    for r in range(0, 3):
        for c in range(0, 3):
            # See if cell is empty
            if (grid[r][c] == '_'):
                # Make move
                grid[r][c] = ai_el
                # Check minimax value
                val = minimax(grid, 0, True, pl_el, ai_el)
                # Undo move
                grid[r][c] = '_'

                # If value of this move is greater than best value, update
                if (val < best_val):  # I THOUGHT WE WANTED SMALLEST VALUE THO???
                    best_val = val
                    best_move = (r, c)
    
    # After checking minimax for everything, return best move
    return best_move

