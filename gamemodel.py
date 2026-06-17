import sys

class TicTacGame:
    """ a game of Tic Tac Toe intentionally made extensible """
    def __init__(self):
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.player1 = "X"
        self.player2 = "O"

    def choose_move(self, player, x, y):
        self.board[x][y] = player

    def row_to_str(self, pos):
        out = ""
        for c in self.board[pos]:
            out += c
            out += "|"
        return out[:-1]
    def print_board(self):
        for i in range(3):
            print(self.row_to_str(i))
            
