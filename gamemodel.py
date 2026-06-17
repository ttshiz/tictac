import sys

class TicTacGame:
    """ a game of Tic Tac Toe intentionally made extensible """
    def __init__(self):
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.player1 = "X"
        self.player2 = "O"

    def choose_move(self, player, x, y):
        self.board[x][y] = player

    def check_win(self, plyr):
        for i in self.board:
            row = set(i)
            row.add(plyr)
            if len(row) == 1:
                return True
        for i in range(3):
            col = set(plyr)
            for j in range(3):
                col.add(self.board[j][i])
            if len(col) == 1:
                return True
        backdiag = set(plyr)
        for i in range(3):
            backdiag.add(self.board[i][i])
        if len(backdiag) == 1:
            return True
        fordiag = set(plyr)
        for i in range(3):
            fordiag.add(self.board[i][2-i])
        if len(fordiag) == 1:
            return True
        return False
            
    def row_to_str(self, pos):
        out = ""
        for c in self.board[pos]:
            out += c
            out += "|"
        return out[:-1]
        
    def print_board(self):
        for i in range(3):
            print(self.row_to_str(i))
            
