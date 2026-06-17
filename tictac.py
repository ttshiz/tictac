import curses
import gamemodel
from curses import wrapper

def main(stdscr):
    # initialize game 
    #gm = gamemodel.TicTacGame()
    #gm.print_board()
    stdscr.clear()
    row1 = " | | "
    row2 = " | | "
    row3 = " | | "
    gm = [row1, row2, row3]
    
    stdscr.addstr(0, 0, row1)
    stdscr.addstr(1, 0, row1)
    stdscr.addstr(2, 0, row1)
    stdscr.refresh()

    # game loop
    for i in range(9):
        # TODO: add input checking
        stdscr.addstr(3, 0, "Player symbol?") 
        plyr = stdscr.getkey()
        stdscr.refresh()
        stdscr.addstr(4, 0, "row?") 
        row = stdscr.getkey()
        stdscr.addstr(5, 0, "column?") 
        column = stdscr.getkey()
        stdscr.addstr(6, 0, "Player {} requested ({},{})".format(plyr, row, column))

        gm[row][column]= plyr

        stdscr.addstr(0, 0, row1)
        stdscr.addstr(1, 0, row1)
        stdscr.addstr(2, 0, row1)

wrapper(main)