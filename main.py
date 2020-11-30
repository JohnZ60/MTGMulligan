# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:37:48 2020
What does the program do?
    Takes a deck provided and simulates play with the starting hand to
    determine if the starting hand should be mulliganed.

open-mtg MIT license granted by Hylnur Davíð Hlynsson for simulating the game (https://github.com/hlynurd/open-mtg)
Original simulator coded by Hylnur and Erik Martinez, modified by Alexander Mains, Johnathan Tan

What was added?
Additional decks and implementation of those decks in deck.py and game.py
Changed implementation of the original Monte Carlo Tree Search to play the game
An additional Monte Carlo Tree Search algorithm to determine mulligans within monteCarloTreeSearch.py
Added Artifact card type in cards.py


@author: Alexander Mains
"""
import random
#imported models
from numpy import loadtxt
from enum import Enum
import logging
import os

import game
import mcts
import player
import deck


"""
class cardName(object):
    def __init__(self):
        self.name = "cardName"
        self.cmc = "costToCast(example 3R is 3 colorless and 1 red)"
        self.power = power
        self.toughness = toughness
        self.rulesText = "CopyOfRulesText"
"""



def configure_logging():
    """
    Configures logging
    :return:
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("[%(levelname)-5.5s]  %(message)s"))
    file_handler = logging.FileHandler("..\open_mtg.log", 'a', 'utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter("%(asctime)s  [%(levelname)-5.5s]  %(message)s"))

    # code for later when stream output level can be set by command line argument
    """
    if args.verbose:
        stream_handler.setLevel(logging.INFO)
    elif args.silent:
        stream_handler.setLevel(logging.ERROR)
    elif args.debug:
        stream_handler.setLevel(logging.DEBUG)
    else:
        stream_handler.setLevel(logging.WARNING)
    """

    root_logger.addHandler(stream_handler)
    root_logger.addHandler(file_handler)


def start_games(amount_of_games):
    player_a_wins = 0
    player_b_wins = 0
    games_played = 0

    #logging.info("Starting Open MTG. Playing {0} games".format(amount_of_games))
    for i in range(amount_of_games):
        gold_deck = deck.get_8ed_core_gold_deck()
        silver_deck = deck.get_8ed_core_silver_deck()
        current_game = game.Game([player.Player(gold_deck), player.Player(silver_deck)])
        current_game.start_game()
        #if current_game.active_player.index == 0:
        #    logging.info("Gold player starts game")
        #else:
        #    logging.info("Silver player starts game")
            
        while not current_game.is_over():
            if current_game.player_with_priority.index == 1:
                move = current_game.player_with_priority.determine_move(method="random", game=current_game)
            else:
                # move = game.player_with_priority.determine_move(method="random", game=game)
                if len(current_game.get_moves()) == 1:
                    move = current_game.get_moves()[0]
                else:
                    move = mcts.uct(current_game, itermax=5)

            current_game.make_move(move, False)

        if current_game.players[1].has_lost:
            player_a_wins += 1
        elif current_game.players[0].has_lost:
            player_b_wins += 1
        games_played += 1
        logging.info("Game {0} is over! current standings: "
                     "{1} - {2}".format(games_played, player_a_wins, player_b_wins))

    logging.info("Player A won {0} out of {1}".format(player_a_wins, games_played))
    logging.info("Player B won {0} out of {1}".format(player_b_wins, games_played))
    #logging.info("Quitting Open MTG{0}{0}".format(os.linesep))


if __name__ == "__main__":
    try:
        configure_logging()
        start_games(10)
    except SystemExit:
        pass
    except KeyboardInterrupt:
        logging.error("Open-mtg stopped by Keyboard Interrupt{0}{0}".format(os.linesep))
    except:
        logging.exception("Unexpected exception")




