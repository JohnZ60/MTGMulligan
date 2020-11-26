""" Title: Introduction to Monte Carlo Tree Search
Author: Jeff Bradberry
Date: 11/23/2020
Code version: Unknown
Availability: http://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/
"""
import random
import datetime
from random import choice
from __future__ import division
from math import log, sqrt

class MonteCarloTreeSearch:
    def __init__(self, game, **kwargs):
        #Takes an instance of a Game and optionally some keyword arguments.
        #Initialize the list of game states and the statistics tables.
        #TODO: create game class
        self.game = game
        self.states = []
        seconds = kwargs.get('time', 30)
        self.calculationTime = datetime.timedelta(seconds = seconds)
        self.maxMoves = kwargs.get('maxMoves', 100)

        #Dicitionaries containing the counts for every game state that is being tracked
        self.wins = {}
        self.plays = {}

        #Larger values of C will encourage more exploration of the possibilities,
        #and smaller values will cause the AI to prefer concentrating on known good moves.
        self.C = kwargs.get('C', 1.4)


    def update(self, state):
        #Takes a game state, and appends it to the history
        self.states.append(state)

    def getPlay(self):
        #Causes the AI to calculate the best move from
        #the current game state and return it
        self.maxDepth = 0
        state = self.states[-1]
        player = self.game.currentPlayer(state)
        legal = self.game.legalPlays(self.states[:])

        #Bail out early if there is no real choice to be made
        if not legal:
            return
        if len(legal) == 1:
            return legal[0]

        games = 0

        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.calculationTime:
            self.runSimulation()
            games += 1

        movesStates = [(p, self.game.nextState(state,p)) for p in legal]

        #Display the number of calls of 'runSimulation' and the time elapsed.
        print (games, datetime.datetime.utcnow() - begin)

        #Pick the move with the highest percentage of wins.
        percentWins, move = max(
            (self.wins.get((player, S), 0) / self.plays.get((player, S), 1), p)
            for p, S in movesStates
        )

        #Display the stats for each possible play.
        for x in sorted(
            ((100 * self.wins.get((player, S), 0) / self.plays.get((player, S), 1),
            self.wins.get((player, S), 0),
            self.playes.get((player, S), 0), p)
            for p, S in movesStates),
            reverse = True
        ):
            print ("{3}: {0:.2f}% ({1}/{2})".format(*x))

        print ("Maximum depth searched:", self.maxDepth)

        return move


    def runSimulation(self):
        #Plays out a "random" game from the current position,
        #then updates the statistics tables with the result.

        #optimization, use local variable lookup instead of attribute access each loop
        plays, wins = self.plays, self.wins

        visitedStates = set()
        simulatedStates = self.states[:]
        state = simulatedStates[-1]
        #TODO: game needs a method currentPlayer(state)
        player = self.game.currentPlayer(state)

        expand = True
        for t in range(1, self.maxMoves + 1):
            #legal is the list legal moves that the player can take
            #TODO: game needs a method legalPlays(state) that returns a list of legal moves(attack/place cards...)
            legal = self.game.legalPlays(simulatedStates)
            #TODO: game nees a method nexState(state, play) that creates a new state, given the state and the move applied to it
            movesStates = [(p, self.game.nextState(state, p)) for p in legal]

            #Use confidence interval formula to choose which move to take: meanPayOutForMachine +- sqrt(2 * Ln(numOfPlays) / numOfPlaysOfMachine)
            #This formula adds together two parts. The first part is just the win ratio,
            #but the second part is a term that grows slowly as a particular move remains neglected.
            #Eventually, if a node with a poor win rate is neglected long enough, it will begin to be chosen again.
            #This term can be tweaked using the configuration parameter C added to __init__ above.
            if all(plays.get((player, S)) for p, S in movesStates):
                #If we have stats on all of the legal moves here, use them.
                logTotal = log(sum(plays[(player, S)] for p, S in movesStates))
                value, move, state = max(
                    ((wins[(player, S)] / plays[(player, S)]) + 
                     self.C * sqrt(logTotal / plays[(player, S)]), p, S)
                    for p, S in movesStates
                )
            else:
                #Otherwise choose a random move
                move, state = choice(movesStates)

            simulatedStates.append(state)

            #If current state is the first new one this function have encountered
            if expand and (player, state) not in self.playes:
                expand = False
                self.plays[(player,state)] = 0
                self.wins[(player,state)] = 0
                if t > self.maxDepth:
                    self.maxDepth = t

            visitedStates.add((player,state))

            player = self.game.currentPlayer(state)
            #TODO: game needs a method winner(state) that returns a winner? or a boolean to signal the end of game?
            winner = self.game.winner(simulatedStates)
            if winner:
                break

            for player, state in visitedStates:
                if (player,state) not in self.plays:
                    continue
                self.plays[(player,state)] += 1
                if player == winner:
                    self.wins[(player,state)] += 1
