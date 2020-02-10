import sys
import os

class game():

    def __init__(self, players):
        self.players = players

    def play_n_rounds(self, rounds = 1):
        return [self.play() for i in range(rounds)]
    
    def play(self):
        raise('play not implemented in child class')

    