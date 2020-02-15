import sys
import os
import random

from tournament import tournament as T
from tournament import game as G

class connect4(G.game):
    
    cols = None
    rows = None
    board = []

    def __init__(self, cols = 7, rows = 6):
        self.rows = rows
        self.cols = cols
        self.clear_board()

    def clear_board(self):
        self.board = [[0] * self.cols] * self.rows
    
    def is_game_over(self):
        if self.who_won() is not None:
            return True
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True

    def who_won(self):
        b = self.board
        for r in range(len(b)):
            for c in range(len(b[r])):
                # check horizontal
                if c + 3 < len(b[r]):
                    if b[r][c] == b[r][c+1] and b[r][c] == b[r][c+2] and b[r][c] == b[r][c+3]:
                        return b[r][c] 
                # check verticle
                if r + 3 < len(b):
                    if b[r][c] == b[r+1][c] and b[r][c] == b[r+2][c] and b[r][c] == b[r+3][c]:
                        return b[r][c]
                # check diagonal down
                if c + 3 < len(b[r]) and r + 3 < len(b):
                    if b[r][c] == b[r+1][c+1] and b[r][c] == b[r+2][c+2] and b[r][c] == b[r+3][c+3]:
                        return b[r][c]
                # check diagonal up
                if c + 3 < len(b[r]) and r > 3:
                    if b[r][c] == b[r-1][c+1] and b[r][c] == b[r-2][c+2] and b[r][c] == b[r-3][c+3]:
                        return b[r][c]
        return None

    def valid_moves(self):
        moves = set(range(len(self.board[0])))
        moves -= set([i for i in moves if self.board[0][i] != 0])
        return moves
        
    def make_move(self, move, player):
        for row in range(len(self.board())):
            if self.board[row][move] != 0:
                self.board[row-1][move] = player
                return
        self.board[len(self.board)-1][move] = player
        return

    def player_mask(self, player):
        

    def play(self, players, max_turn_number, max_turn_time):
        random.seed()
        random.shuffle(players)
        self.clear_board()

        while(self.is_game_over == False):
            moves = self.valid_moves()
            if moves is not None:
                move = players[0].take_turn(time_limit=max_turn_time)
                if move in moves:
                    self.make_move(move, id(players[0]))
                else:
                    # invalid move player 0 looses
                    return [id(players[1]),id(players[0])]
            else:
                # return players in shuffled order (should eventuallyu sort by total tuirn time)
                return [id(players[0]),id(players[1])] 

        outputs = map(lambda x: x.take_turn(time_limit=max_turn_time), players)
        moves = list(map(lambda x, y:(x,y), players, outputs))

        # sort is stable so we sort by secondardy key and then primary key
        moves.sort(reverse=False, key = lambda x: x[1][0]) # sort by time less is better
        moves.sort(reverse=True, key = lambda x: x[1][1]) # sort by value returned more is better
        return list(map(lambda x: id(x[0]), moves))

    

tor = T.tournament(players_path='./players/C4/connect4_players.csv', max_turn_time=1, history_path='history.txt')
tor.game = connect4()
print(tor)
print()
tor.play_all_player_combinations(games=2, min=2, max=2)
print(tor)
tor.save_history()