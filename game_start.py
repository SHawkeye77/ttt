"""
Samuel Hohenshell
File contains function(s) for starting the game up
"""
import ttt


# Sets global variables for pl_el and ai_el to 'x' and 'o' values
# Returns "True" if player goes first, "False" if player goes second
def game_start():
    f_or_s = input("\nWelcome! Do you want to "\
        "go first or second? ").strip().lower()
    
    while True:
        if (f_or_s == "first"):
            first = True
            break
        elif (f_or_s == "second"):
            first = False
            break
        else:
            f_or_s = input("Command not recognized.\n"\
                "Would you like to go first or second? ").strip().lower()
    
    print("Thank you!\n")
    x_or_o = input("Would you like to be \"X\" or \"O\"? ").strip().lower()
    while True:
        if (x_or_o == 'x'):
            pl_el = 'x'
            ai_el = 'o'
            return (first, pl_el, ai_el)
        elif (x_or_o == 'o'):
            pl_el = 'o'
            ai_el = 'x'
            return (first, pl_el, ai_el)
        else:
            x_or_o = input("Command not recognized. "\
                "Would you like to be \"X\" or \"O\"? ").strip().lower()

