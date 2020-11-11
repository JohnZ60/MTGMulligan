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
from keras.models import Sequential
from keras.layers import Dense


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
        
        
class Land():
    def __init__(self, name, value, rulesText, sickness):
        self.name = name
        self.value = value
        self.rulesText = rulesText #What does the card do, For debugging and laziness
        self.sickness = sickness #If the rules text doesn't have Haste, put false
        self.tap = False
    
class Card(object):
    def __init__(self, name, value, cmc, power, toughness, rulesText, sickness):
        self.name = name
        self.cmc = cmc
        self.power = power
        self.toughness = toughness
        self.rulesText = rulesText
        self.sickness = sickness #If the rules text has Haste, put false
        
        
        

    # Implementing build in methods so that you can print a card object
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

    # Generate 52 cards
    def build(self):
        #self.cards = [] don't think I need this here
        for i in ['Hearts', 'Clubs', 'Diamonds']: #count to 3
            self.cards.append(Card('Fervent Champion', 1, "R" , 1, 1, 'First strike, haste \nWhenever Fervent Champion attacks, another target attacking Knight you control gets +1/+0 until end of turn. \nEquip abilities you activate that target Fervent Champion cost 3 less to activate.\n', False))
            self.cards.append(Card('Scorch Spitter', 1, "R", 1, 1, 'Whenever Scorch Spitter attacks, it deals 1 damage to the player or planeswalker it\'s attacking.', True))
            self.cards.append(Card('Rimrock Knight', 2, "1R", 3, 1, 'R : Target Creature gets +2/+0 until end of turn,\n Rimrock Knight can\'t block.', True))
            self.cards.append(Card('Robber of the Rich', 3, '1R', 2, 2, 'Reach, haste\nWhenever Robber of the Rich attacks, if defending player has more cards in hand than you, exile the top card of their library. \nDuring any turn you attacked with a Rogue, you may cast that card and you may spend mana as though it were mana of any color to cast that spell.', False))
            self.cards.append(Card('Runaway Steam-Kin', 3, '1R', 1, 1, rulesText, True))
            self.cards.append(Card('Anax, Hardened in the Forge', 3, '1RR', 0, 3, rulesText, True))
            self.cards.append(Card('Bonecrusher Giant', 4, '2R', 4, 3, rulesText, True))
            self.cards.append(Card('Torbran, Thane of Red Fell', 5, '1RRR', 2, 4, rulesText, True))
            self.cards.append(Card('Claim the Firstborn', 1, 'R', 2, 2, rulesText, False))
            self.cards.append(Card('Embercleave', 6, '4RR', 0, 0, rulesText, False))
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
        print ("Player's hand: {}".format(self.hand))
        return self

    def discard(self):
        return self.hand.pop()
    
    
    




# Testing the model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#The x needs to be the array of inputs whilst Y needs to be array of outputs
#x = []
#y = []
#model.fit(x, y, epochs =50; batch_size=10)

# Test making a Card
card = Card('Spades', 6)
print(card)

# Test making a Deck
myDeck = Deck()
myDeck.shuffle()
# deck.show()

PlayerOne = Player("One")

PlayerOne.sayHello()
PlayerOne.draw(myDeck, 7)
PlayerOne.showHand()

