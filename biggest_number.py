import sys
import os
from tournament import tournament as T
from tournament import game as G

class biggest_number(G.game):

    def play(self, players, max_turn_number, max_turn_time):
        outputs = map(lambda x: x.take_turn(time_limit=max_turn_time), players)
        moves = list(map(lambda x, y:(x,y), players, outputs))

        # sort is stable so we sort by secondardy key and then primary key
        moves.sort(reverse=False, key = lambda x: x[1][0]) # sort by time less is better
        moves.sort(reverse=True, key = lambda x: x[1][1]) # sort by value returned more is better
        return list(map(lambda x: id(x[0]), moves))

    

tor = T.tournament(players_path='./players/players.csv', max_turn_time=1, history_path='history.txt')
tor.load_history()
print(tor)
print()
tor.game = biggest_number()
tor.play_game()
print(tor)
print()
tor.play_n_games(5)
print(tor)
print()
tor.play_all_player_combinations()
print(tor)
print()
tor.save_history()