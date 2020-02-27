import os
import time

class player():

    path = ''
    player_name = ''
    author = ''
    score = 0

    def __init__(self, path, player_name = '', author=''):
        self.path = path
        self.player_name = player_name
        self.author = author

    def take_turn(self, data = None, time_limit=None):
        self.clean_directory()
        script = ''
        if time_limit is not None:
            script += 'timeout {limit}s '.format(limit = time_limit)
        if data is not None:
            f = open('./input.txt', 'w')
            f.write(str(data))
            script += 'cat ./input.txt | '
        script += self.path +' > ./output.txt'
        start_time = time.time()
        os.system(script)
        end_time = time.time()
        if os.path.exists('./output.txt'):
            f = open('./output.txt', 'r')
        else:
            self.clean_directory()
            return (end_time - start_time, '')
        lines = f.readlines()
        self.clean_directory()
        return (end_time - start_time, lines)

    def clean_directory(self):
        pass
        # if os.path.exists('./output.txt'):
        #     os.remove('./output.txt')
        # if os.path.exists('./input.txt'):
        #     os.remove('./input.txt')

    def set_score(self, n):
        self.score = n

    def __str__(self):
        cols = [round(100 * self.score, 2), self.author, self.player_name, self.path]
        return ' | '.join([str(c) for c in cols])
