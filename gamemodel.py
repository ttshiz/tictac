import sys

class TicTacGame:
    """ a game of Tic Tac Toe intentionally made extensible """
    def __init__(self):
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.player1 = "X"
        self.player2 = "O"

    def choose_move(self, player, x, y):
        self.board[x][y] = player

    def print_board(self):
        for i in self.board:
            print(i)

def main():
    # initialize game 
    gm = TicTacGame()
    gm.print_board()

    # game loop
    for i in range(9):
        # TODO: add input checking
        (plyr, thisx, thisy) = sys.arg[1]
        print("Player {} requested ({},{})".format(plyr, thisx, thisy))
        gm.choose_move(plyr, thisx, thisy)
        gm.print_board()

if __name__ == "__main__":
    main()