import sys
import os
from tournament import tournament as T
from tournament import game as G

tor = T.tournament(players_path='./players.csv')
print(tor)


class biggest_number(game):

    def __init__(self, players):
        self.players = players

    def play_n_rounds(self, rounds = 1):
        return [self.play() for i in range(rounds)]
    
    def play(self):
        outputs = self.players.map(take_turn)
        moves = list(map(lambda x, y:(x,y), self.players, outputs))
        moves.sort(key = lambda x: x[1])
        return list(map(lambda x: x[0].path))

    