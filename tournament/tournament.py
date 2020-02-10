import player

class tournament():

    players = []
    challenge = ''

    def __init__(self, challange_path=None, players_path=None):
        self.challange = challange_path
        if players_path is not None:
            self.load_players(players_path)

    def load_players(self, path):
        f = open(path)
        self.participants = []
        for line in f:  
            cols = line.split(',')
            cols = [col.strip() for col in cols]         
            self.players += [player(path = cols[2], player_name = cols[1], author=cols[0])]

    def __str__(self):
        lines = [str(p) for p in self.players]
        return '\n'.join(lines)


