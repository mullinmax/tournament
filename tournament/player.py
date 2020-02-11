import os

class player():

    path = ''
    player_name = ''
    author = ''
    score = 0

    def __init__(self, path, player_name = '', author=''):
        self.path = path
        self.player_name = player_name
        self.author = author

    def take_turn(self, data = None):
        self.clean_directory()
        if data is not None:
            f = open('./input.txt', 'w')
            f.write(data)
            os.system('cat ./input.txt | ' + self.path +' > ./output.txt')
            f = open('./output.txt', 'r')
            lines = f.readlines()
        else:
            os.system(self.path +' > ./output.txt')
            f = open('./output.txt', 'r')
            lines = f.readlines()
        self.clean_directory()
        return lines

    def clean_directory(self):
        if os.path.exists('./output.txt'):
            os.remove('./output.txt')
        if os.path.exists('./input.txt'):
            os.remove('./input.txt')

    def set_score(self, n):
        self.score = n

    def __str__(self):
        cols = [round(100 * self.score, 2), self.author, self.player_name, self.path]
        return ' | '.join([str(c) for c in cols])
