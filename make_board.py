# Samuel Hohenshell
# 3/9/2020

import pygame
import ttt

# Draws the current state of board "grid" to "screen"
# "user" is either x or o, ai is the other
def draw_board(screen, grid, pl_el, ai_el):

    # Setting correct x's and o's
    if (pl_el == 'x'):
        x = pygame.image.load('./images/white_x.png') # Player   = X
        o = pygame.image.load('./images/green_o.png') # Computer = O
    elif (pl_el == 'o'):
        o = pygame.image.load('./images/white_o.png') # Player   = O
        x = pygame.image.load('./images/green_x.png') # Computer = X
    else:
        exit(1)

    # Drawing board
    screen.fill((0,0,0)) # Color display surface black
    
    # Drawing grid
    pygame.draw.rect(screen, (255,255,255), (100,5,5,290))
    pygame.draw.rect(screen, (255,255,255), (200,5,5,290))
    pygame.draw.rect(screen, (255,255,255), (5,100,290,5))
    pygame.draw.rect(screen, (255,255,255), (5,200,290,5))

    # Drawing X's and O's according to "grid"
    for r, row in enumerate(grid):
        for c, col in enumerate(grid[r]):
            # Currently at grid[r][c]
            if grid[r][c] == pl_el:   # User occupies
                if pl_el == 'x':
                    screen.blit(x, (13+(100*c), 13+(100*r))) 
                else:
                    screen.blit(o, (13+(100*c), 13+(100*r))) 
            elif grid[r][c] == ai_el: # AI occupies
                if pl_el == 'x':
                    screen.blit(o, (13+(100*c), 13+(100*r))) 
                else:
                    screen.blit(x, (13+(100*c), 13+(100*r))) 


# Takes in "screen" a board "grid", a (row,col) location "move_loc" and 
#   a boolean "change_to"
def move(move_loc, change_to, grid):
    r = move_loc[0]
    c = move_loc[1]
    if (grid[r][c] == '_'):  # If its unoccupied
        grid[r][c] = change_to
        return (True, grid)
    else:
        return (False, grid)


# Changes (x,y) move into (row, column) move and changes "grid" according
#   to a click on that position
# Should only be called by a player
def deal_with_mouseclick(pos, pl_el, grid):
    x = pos[1]  # Band-aid (sorry if you're reading this)
    y = pos[0]

    # (0,0)
    if ((x < 95) and (x > 5) and (y < 95) and (y > 5)):
        return move((0,0), pl_el, grid)
    # (1,0)
    elif ((x < 195) and (x > 105) and (y < 95) and (y > 5)):
        return move((1,0), pl_el, grid)
    # (2,0)
    elif ((x < 295) and (x > 205) and (y < 95) and (y > 5)):
        return move((2,0), pl_el, grid)
    # (0,1)
    elif ((x < 95) and (x > 5) and (y < 195) and (y > 105)):
        return move((0,1), pl_el, grid)
    # (1,1)
    elif ((x < 195) and (x > 105) and (y < 195) and (y > 105)):
        return move((1,1),pl_el, grid)
    # (2,1)
    elif ((x < 295) and (x > 205) and (y < 195) and (y > 105)):
        return move((2,1), pl_el, grid)
    # (0,2)
    elif ((x < 95) and (x > 5) and (y < 295) and (y > 205)):
        return move((0,2), pl_el, grid)
    # (1,2)
    elif ((x < 195) and (x > 105) and (y < 295) and (y > 205)):
        return move((1,2), pl_el, grid)
    # (2,2)
    elif ((x < 295) and (x > 205) and (y < 295) and (y > 205)):
        return move((2,2), pl_el, grid)

