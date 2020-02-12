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

    def play_all_player_combinations(self, games = 1, min = 2, max = None, inter_author=True, intra_author=True, self_play=True):
        if max is None:
            max = len(self.players)
        player_combos = []
        for n in range(min, max + 1):
            player_combos += self.get_all_n_player_combinations(self.players, n)
        player_lists = self.player_list_checker(player_combos, inter_author, intra_author, self_play)
        for pl in player_lists:
            self.play_n_games(n, players = pl)

    def get_all_n_player_combinations(self, player_list, n):
        if n > len(player_list):
            return []
        if n == 1:
            return [[p] for p in player_list]
        if n < 1:
            return []
        out = []
        for i in range(len(player_list)):
            for l in self.get_all_n_player_combinations(player_list[i:], n-1):
                out.append([player_list[i]] + l)
        return out

    def player_list_checker(self, player_lists, inter_author=True, intra_author=False, self_play=False):
        clean_player_lists = []
        for pl in player_lists:
            distinct_authors = sum([1 for author in set(map(lambda p: p.author, pl))])
            if inter_author == False and distinct_authors > 1:
               pass
            elif intra_author == False and distinct_authors < len(pl):
                pass
            elif self_play == False and sum([1 for player in set(map(lambda p: id(p), pl))]) < len(pl):
                pass
            else:
                clean_player_lists.append(pl)
        return clean_player_lists

    def play_n_games(self, n, players=None):
        if players is None:
            for i in range(n):
                self.play_game()
        else:
            for i in range(n):
                self.play_game(players)

    def play_game(self, players=None):
        if players is None:
            ranked_ids = self.game.play(self.players)
        else:
            ranked_ids = self.game.play(players)
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


