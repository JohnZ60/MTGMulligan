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

#class Battlefield():
    def__init__(self):
        
    
#class Land():

class Card(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        

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
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            self.cards.append(Card(suit, val))

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
    def __init__(self, name):
        self.name = name
        self.hand = []
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

