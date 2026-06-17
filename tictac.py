import curses
import gamemodel
from curses import wrapper

def main(stdscr):
    # initialize game 
    gm = gamemodel.TicTacGame()
    gm.print_board()
    stdscr.clear()
 
    for i in range(3):
        stdscr.addstr(i, 0, gm.row_to_str(i))

    # game loop
    for i in range(9):
        # TODO: add input checking
        stdscr.addstr(3, 0, "Player symbol?") 
        plyr = stdscr.getkey()
        stdscr.addstr(4, 0, "row?") 
        row = stdscr.getkey()
        stdscr.addstr(5, 0, "column?") 
        column = stdscr.getkey()
        stdscr.addstr(6, 0, "Player {} requested ({},{})".format(plyr, row, column))

        gm.choose_move(plyr, int(row), int(column))
        for i in range(3):
            stdscr.addstr(i, 0, gm.row_to_str(i))

wrapper(main)