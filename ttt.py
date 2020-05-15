"""
Unbeatable Tic-Tac-Toe AI
Samuel Hohenshell

Notes:
Minimizer = AI    = -10
Maximizer = Human =  10
"""

import pygame
import make_board
import minimax
import game_start
import time
import sys


def main():
    """ Variables used in our game """

    keep_going = True

    # Character representing the player
    pl_el = 'q'

    # Character representing the ai
    ai_el = 'q'

    # Represents the current state of the grid
    grid = [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]

    pygame.init()
    # first is True if player goes first, False if player goes second
    (first, pl_el, ai_el) = game_start.game_start()

    # Creating display surface object with specified width/height
    screen = pygame.display.set_mode((300, 300)) 
    pygame.display.set_caption('Unbeatable Tic-Tac-Toe')  # Window name

    # create the pygame clock to run in our loop
    clock = pygame.time.Clock()

    # Holds while it is the user's turn
    if (first != None):
        user_turn = first
    else:
        exit(1)
    print("\nClick on the pygame window to play. Good luck!")

    ############################# Main game loop ##############################
    while True:
        clock.tick(30)       # Running program at 30 fps
        make_board.draw_board(screen, grid, pl_el, ai_el)
        pygame.display.update()
        if (not keep_going):
            break
        ###################### Dealing with USER's play ######################
        while user_turn:
            # Checking for pygame events
            events = pygame.event.get()
            for event in events:
                # If I click the "x" to close window, quit pygame and program
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    quit() 
                # Handle mouse click
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    user_turn, grid = (make_board.deal_with_mouseclick(pos, pl_el, grid))
                    user_turn = not user_turn

            # Checking if user won
            if (minimax.evaluate(grid, pl_el, ai_el) == 10):
                print("\n***** USER won *****")
                keep_going = False
                break
            elif (minimax.evaluate(grid, pl_el, ai_el) == -10):
                print("\n***** AI won, the singularity is upon us! *****\nThe game window will close in 30 seconds")
                keep_going = False
                break
            else: 
                if (not minimax.moves_left(grid)):
                    print("\n***** It's a draw! *****\nThe game window will close in 30 seconds")
                    keep_going = False
                    break

        ##################### Dealing with AI's play #####################
        while (not user_turn) and (keep_going):
            # Gets "best_move" which is (row, column) of best possible ai move
            best_move = minimax.get_best_move(grid, pl_el, ai_el)
            # Making the move
            user_turn, grid = make_board.move(best_move, ai_el, grid)

            # Checking if AI won or tie
            if (minimax.evaluate(grid, pl_el, ai_el) == 10):
                print("\n***** USER won *****")
                keep_going = False
                break
            elif (minimax.evaluate(grid, pl_el, ai_el) == -10):
                print("\n***** AI won, the singularity is upon us! *****\nThe game window will close in 30 seconds")
                keep_going = False
                break
            else: 
                if (not minimax.moves_left(grid)):
                    print("\n***** It's a draw! *****\nThe game window will close in 30 seconds")
                    keep_going = False
                    break
        pygame.display.update()

    # Sleeping so the user can see how they lost/drew
    for x in range(30):
        print(str(x+1) + " ", end="")
        sys.stdout.flush()
        time.sleep(1)
    print("")
    # Shutting pygame and the program
    pygame.quit()
    return


# Running if this is called
if __name__ == '__main__':
    main()

