from .player import player
from .game import game
from multi_elo import calc_elo

class tournament():

    players = []
    challenge = ''
    game = game()

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

        if self.game is not None:
            self.game.players = self.players

    def play_n_games(self, n):
        for i in range(n):
            self.play_game()
    
    def play_game(self):
        ranked_ids = self.game.play(self.players)
        self.update_scores(ranked_ids)

    def update_scores(self, ranked_ids):
        ranked_players = self.get_players_by_id(ranked_ids)
        scores = [1] + list(map(lambda p: p.score, ranked_players)) + [0]
        new_scores = []
        for i in range(len(scores)-2):
            new_scores += [(scores[i] + 2*scores[i+1] + scores[i+2]) / 4]
        for i in range(len(ranked_players)):
            ranked_players[i].score = new_scores[i]

    def get_players_by_id(self, ids):
        players = []
        for id_num in ids:
            p = self.get_player_by_id(id_num)
            players += [p]
        return players

    def get_player_by_id(self, id_num):
        for p in self.players:
            if id(p) == id_num:
                return p
        # we need to raise in this case because we can no longer preserve order
        raise Exception('Player not found with specified id: ' + str(id_num))
    
    def set_game(self, game):
        self.game = game
        self.game.players = self.players

    def __str__(self):
        lines = [str(p) for p in self.players]
        return '\n'.join(lines)


