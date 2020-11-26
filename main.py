# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:37:48 2020
What does the program do?
    Takes a deck provided and simulates play with the starting hand to
    determine if the starting hand should be mulliganed.




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

class Battlefield(object):
    def __init__(self):
        self.cardsOne = [] #Cards On the field for P1
        self.cardsTwo = [] #Cards On the field for P2 (UNUSED BUT HERE FOR CLARITY)
        self.landsOne = [] #Lands for player one
        self.landsTwo = [] #Lands for player two (UNUSED BUT HERE FOR CLARITY)
        self.turn = 1  #turn counter
        self.exileOne = [] #Player One's exile
        self.exileTwo = [] #Player Two's exile
        self.graveyardOne = [] #Player One Graveyard
        self.graveyardTwo = [] #Player Two graveyard
        

class Land():
    def __init__(self, name, value, color, rulesText, sickness):
        self.name = name #name of the land
        self.value = value #value of the card for testing
        self.color = color #color the land taps for
        self.rulesText = rulesText #What does the card do, For debugging and laziness
        self.sickness = sickness #If the rules text doesn't have Haste/or if it comes in tapped, put false
        self.tap = False #is the land tapped?
    
        # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return self.show()
        
    def show(self):

        return self
    
    
class Card(object):
    def __init__(self, name, value, cmc, cost, power, toughness, rulesText, sickness):
        self.name = name
        self.cmc = cmc #total mana number to cast the spell
        self.cost = cost #Actual cost to cast the spell, with color
        self.power = power #How much damage can it do? (If 0, it's a noncreature for our cases)
        self.toughness = toughness #How much damage can this thing take (if 0, it's a noncreature)
        self.rulesText = rulesText #What does the card do, for debugging and laziness
        self.sickness = sickness #If the rules text has Haste, put false
        self.tap = False #Is the thing tapped
        
        
        

    # Implementing built in methods so that you can print a card object
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return self.show()
        
    def show(self):

        return self


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print (card.show())

    # Generate 60 cards in the deck
    def build(self):
        #self.cards = [] don't think I need this here
        self.cards.append(Card('Fervent Champion', 1, 1, "R" , 1, 1, 'First strike, haste \nWhenever Fervent Champion attacks, another target attacking Knight you control gets +1/+0 until end of turn. \nEquip abilities you activate that target Fervent Champion cost 3 less to activate.\n', False))
        self.cards.append(Card('Scorch Spitter', 1, 1, "R", 1, 1, 'Whenever Scorch Spitter attacks, it deals 1 damage to the player or planeswalker it\'s attacking.', True))
        self.cards.append(Card('Robber of the Rich', 3, 2, '1R', 2, 2, 'Reach, haste\nWhenever Robber of the Rich attacks, if defending player has more cards in hand than you, exile the top card of their library. \nDuring any turn you attacked with a Rogue, you may cast that card and you may spend mana as though it were mana of any color to cast that spell.', False))
        self.cards.append(Card('Runaway Steam-Kin', 3, 2, '1R', 1, 1, "Whenever you cast a red spell, if Runaway Steam-Kin has fewer than three +1/+1 counters on it, put a +1/+1 counter on Runaway Steam-Kin.\nRemove three +1/+1 counters from Runaway Steam-Kin: Add .", True))
        self.cards.append(Card('Anax, Hardened in the Forge', 3, 3, '1RR', 0, 3, "Anax's power is equal to your devotion to red. (Each  in the mana costs of permanents you control counts toward your devotion to red.)Whenever Anax or another nontoken creature you control dies, create a 1/1 red Satyr creature token with 'This creature can't block.' If the creature had power 4 or greater, create two of those tokens instead.", True))
        self.cards.append(Card('Bonecrusher Giant', 4, 3, '2R', 4, 3, "Stomp 1R: Instant - Adventure: Damage can't be prevented this turn. Stomp deals 2 damage to any target/Whenever Bonecrusher Giant becomes the target of a spell, Bonecrusher Giant deals 2 damage to that spell's controller.", True))
        self.cards.append(Card('Torbran, Thane of Red Fell', 5, 4, '1RRR', 2, 4, "If a red source you control would deal damage to an opponent or a permanent an opponent controls, it deals that much damage plus 2 instead.", True))
        self.cards.append(Card('Embercleave', 6, 6, '4RR', 0, 0, "Flash\nThis spell costs 1 less to cast for each attacking creature you control.\nWhen Embercleave enters the battlefield, attach it to target creature you control.\nEquipped creature gets +1/+1 and has double strike and trample.\nEquip 3 ", False))
        self.cards.append(Land('Castle Embereth', 1, 'R', "Castle Embereth enters the battlefield tapped unless you control a Mountain.Tap: Add R,  1RRTAP: Creatures you control get +1/+0 until end of turn.", True))
        for i in range(1,16):
            self.cards.append(Land('Mountain', 1, 'R', "Tap for 1 red mana", False))
        for i in ['Hearts', 'Clubs', 'Diamonds']: #count to 3
            self.cards.append(Card('Fervent Champion', 1, 1, "R" , 1, 1, 'First strike, haste \nWhenever Fervent Champion attacks, another target attacking Knight you control gets +1/+0 until end of turn. \nEquip abilities you activate that target Fervent Champion cost 3 less to activate.\n', False))
            self.cards.append(Card('Scorch Spitter', 1, 1, "R", 1, 1, 'Whenever Scorch Spitter attacks, it deals 1 damage to the player or planeswalker it\'s attacking.', True))
            self.cards.append(Card('Rimrock Knight', 2, 2, "1R", 3, 1, 'R : Target Creature gets +2/+0 until end of turn,\n Rimrock Knight can\'t block.', True))
            self.cards.append(Card('Robber of the Rich', 3, 2, '1R', 2, 2, 'Reach, haste\nWhenever Robber of the Rich attacks, if defending player has more cards in hand than you, exile the top card of their library. \nDuring any turn you attacked with a Rogue, you may cast that card and you may spend mana as though it were mana of any color to cast that spell.', False))
            self.cards.append(Card('Runaway Steam-Kin', 3, 2, '1R', 1, 1, "Whenever you cast a red spell, if Runaway Steam-Kin has fewer than three +1/+1 counters on it, put a +1/+1 counter on Runaway Steam-Kin.\nRemove three +1/+1 counters from Runaway Steam-Kin: Add .", True))
            self.cards.append(Card('Anax, Hardened in the Forge', 3, 3, '1RR', 0, 3, "Anax's power is equal to your devotion to red. (Each  in the mana costs of permanents you control counts toward your devotion to red.)Whenever Anax or another nontoken creature you control dies, create a 1/1 red Satyr creature token with 'This creature can't block.' If the creature had power 4 or greater, create two of those tokens instead.", True))
            self.cards.append(Card('Bonecrusher Giant', 4, 3, '2R', 4, 3, "Stomp 1R: Instant - Adventure: Damage can't be prevented this turn. Stomp deals 2 damage to any target/Whenever Bonecrusher Giant becomes the target of a spell, Bonecrusher Giant deals 2 damage to that spell's controller.", True))
            self.cards.append(Card('Torbran, Thane of Red Fell', 5, 4, '1RRR', 2, 4, "If a red source you control would deal damage to an opponent or a permanent an opponent controls, it deals that much damage plus 2 instead.", True))
            self.cards.append(Card('Claim the Firstborn', 1, 1, 'R', 2, 2, "Gain control of target creature with converted mana cost 3 or less until end of turn. Untap that creature. It gains haste until end of turn.", False))
            self.cards.append(Card('Embercleave', 6, 6, '4RR', 0, 0, "Flash\nThis spell costs 1 less to cast for each attacking creature you control.\nWhen Embercleave enters the battlefield, attach it to target creature you control.\nEquipped creature gets +1/+1 and has double strike and trample.\nEquip 3 ", False))
            self.cards.append(Land('Castle Embereth', 1, 'R', "Castle Embereth enters the battlefield tapped unless you control a Mountain.Tap: Add R,  1RRTAP: Creatures you control get +1/+0 until end of turn.", True))
            self.cards.append(Land('Mountain', 1, 'R', "Tap for 1 red mana", False))
            

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
            # You can also use the build in shuffle method
            # random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name, deck):
        self.name = name
        self.hand = []
        self.deck = deck
        self.life = 20

    def sayLife(self):
        print ("{} has {} life left".format(self.name,self.life))
        return self

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else: 
                return False
        return True

    # Display all the cards in the players hand
    def showHand(self):
        print ("Player's hand: ")
        for i in self.hand:
            print(str(i) + " ")
        return self

    def discard(self):
        return self.hand.pop()
    



def configure_logging():
    """
    Configures logging
    :return:
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("[%(levelname)-5.5s]  %(message)s"))
    file_handler = logging.FileHandler("open_mtg.log", 'a', 'utf-8')
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

    logging.info("Starting Open MTG. Playing {0} games".format(amount_of_games))
    for i in range(amount_of_games):
        gold_deck = deck.get_8ed_core_gold_deck()
        silver_deck = deck.get_8ed_core_silver_deck()
        current_game = game.Game([player.Player(gold_deck), player.Player(silver_deck)])
        current_game.start_game()

        if current_game.active_player.index == 0:
            logging.info("Gold player starts game")
        else:
            logging.info("Silver player starts game")
        while not current_game.is_over():
            if current_game.player_with_priority.index is 1:
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
    logging.info("Quitting Open MTG{0}{0}".format(os.linesep))


if __name__ == "__main__":
    try:
        configure_logging()
        start_games(2)
    except SystemExit:
        pass
    except KeyboardInterrupt:
        logging.error("Open-mtg stopped by Keyboard Interrupt{0}{0}".format(os.linesep))
    except:
        logging.exception("Unexpected exception")

#The x needs to be the array of inputs whilst Y needs to be array of outputs
#x = []
#y = []
#model.fit(x, y, epochs =50; batch_size=10)

# Test making a Card
card = Land('Mountain', 1, 'R', "Tap for 1 red mana", False)
#print(card)

# Test making a Deck
myDeck = Deck()
myDeck.show()
myDeck.shuffle()


PlayerOne = Player("One", myDeck)

PlayerOne.sayLife()
PlayerOne.draw(myDeck, 7)
PlayerOne.showHand()

PlayerTwo = Player("Two", myDeck)

PlayerTwo.sayLife()
PlayerTwo.draw(myDeck, 7)
PlayerTwo.showHand()

