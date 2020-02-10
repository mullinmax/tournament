import os
from multi_elo import EloPlayer, calc_elo

class player():

    path = ''
    player_name = ''
    author = ''
    place = 0
    score = 1500

    def __init__(self, path, elo=1500, place=0, player_name = '', author=''):
        self.path = path
        self.elo = elo
        self.place = place
        self.player_name = player_name
        self.author = author

    def get_elo_player(self):
        return EloPlayer(place=self.place, elo=self.elo)

    def set_elo_player(self, elo_player):
        self.place = elo_player[0]
        self.elo = elo_player[1]

    def take_turn(self, data = None):
        os.system('rm ./output.txt ./input.txt')
        if data is not None:
            f = open('./input.txt', 'w')
            f.write(data)
            os.system('cat ./input.txt | ' + self.path +' | ./output.txt')
            f = open('./output.txt', 'r')
        else:
            os.system(self.path +' | ./output.txt')
            f = open('./output.txt', 'r')
        return f.readlines()

    def __str__(self):
        cols = [self.place, self.score, self.author, self.player_name, self.path]
        return ' | '.join([str(c) for c in cols])
