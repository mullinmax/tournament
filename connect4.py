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
            print('Someone has won')
            return True
        for row in self.board:
            for col in row:
                if col == 0:
                    print('there is a move left')
                    return False
        print('no more moves')
        return True

    def who_won(self):
        b = self.board
        for r in range(len(b)):
            for c in range(len(b[r])):
                if b[r][c] != 0:
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
        print(move)
        for row in range(len(self.board), 0):
            if self.board[row][move] == 0:
                self.board[row][move] = id(player)
                return
        return

    def player_mask(self, player):
        data = []
        for row in self.board:
            data_row = []
            for col in row:
                if col == id(player):
                    data_row += ['S']
                elif col == 0:
                    data_row += [' ']
                else:
                    data_row += ['O'] 
            data.append(data_row)
        print('data: ' + str(data))
        return data

    def play(self, players, max_turn_number, max_turn_time):
        random.seed()
        random.shuffle(players)
        self.clear_board()
        whos_turn = 0 
        print('Game starts')
        while(self.is_game_over() == False):
            print('it\'s ' + str(whos_turn) + ' turn')
            moves = self.valid_moves()
            print(moves)
            if moves is None: # check for cats game
                return [id(players[0]),id(players[1])] #sort by total runtime eventually 
            player_data = self.player_mask(players[whos_turn])
            print('player_data: ' + str(player_data))
            time, move = players[whos_turn].take_turn(data=player_data, time_limit=max_turn_time)
            move = int(move[0])
            print('move made: ' + str(move))
            if move in moves:
                self.make_move(move, id(players[whos_turn]))
            else:
                # invalid move player 0 looses
                if whos_turn == 0:
                    return [id(players[1]),id(players[0])]
                else:
                    return [id(players[0]),id(players[1])]
            whos_turn = (whos_turn + 1) % 2
            
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