import sys
import os

class game():

    def play_n_rounds(self, rounds = 1):
        return [self.play() for i in range(rounds)]
    
    def play(self, **kwargs):
        raise('play not implemented in child class')
