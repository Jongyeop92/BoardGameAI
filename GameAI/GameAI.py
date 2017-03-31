# -*- coding: utf8 -*-

from __future__ import division

import sys
sys.path.append("../Board")

from Board import *

import copy
import random
import math
import datetime
import pickle


def minimax(state, depth, maxPlayer, firstCall=True):
    result = state.isWin()

    if result != None:
        if result == state.FIRST:
            return INFINITE
        elif result == state.SECOND:
            return -INFINITE
        else:
            return 0
    elif depth == 0:
        return state.getPoint(state.FIRST) - state.getPoint(state.SECOND)

    marker = state.getMaxPlayer(maxPlayer)

    bestInfoList = []
    possiblePositionList = state.getPossiblePositionList(marker)

    for position in possiblePositionList:
        copyState = copy.deepcopy(state)
        copyState.setMarker(marker, position)
        value = minimax(copyState, depth - 1, not maxPlayer, False)

        if bestInfoList == []:
            bestInfoList = [(value, position)]
        else:
            bestValue = bestInfoList[0][0]

            if value == bestValue:
                bestInfoList.append((value, position))
            elif (maxPlayer and value > bestValue) or (not maxPlayer and value < bestValue):
                bestInfoList = [(value, position)]

    if bestInfoList == []:
        return 0

    if firstCall:
        print "bestInfoList:", bestInfoList
        return random.choice(bestInfoList)
    else:
        return bestInfoList[0][0]


def alphabeta(state, depth, alpha, beta, maxPlayer, firstCall=True):
    result = state.isWin()

    if result != None:
        if result == state.FIRST:
            return INFINITE
        elif result == state.SECOND:
            return -INFINITE
        else:
            return 0
    elif depth == 0:
        return state.getPoint(state.FIRST) - state.getPoint(state.SECOND)

    marker = state.getMaxPlayer(maxPlayer)

    bestInfo = None
    possiblePositionList = state.getPossiblePositionList(marker)
    random.shuffle(possiblePositionList)

    for position in possiblePositionList:
        copyState = copy.deepcopy(state)
        copyState.setMarker(marker, position)
        value = alphabeta(copyState, depth - 1, alpha, beta, not maxPlayer, False)

        if maxPlayer and alpha < value:
            alpha = value
            
            if beta <= alpha:
                break

            bestInfo = (alpha, position)
            
        elif not maxPlayer and beta > value:
            beta = value
            
            if beta <= alpha:
                break

            bestInfo = (beta, position)

    if bestInfo == None:
        if maxPlayer:
            value = INFINITE
        else:
            value = -INFINITE

        if firstCall:
            return (value, possiblePositionList[0])
        else:
            return value

    if firstCall:
        return bestInfo
    else:
        return bestInfo[0]


class MonteCarlo(object):

    def __init__(self, **kwargs):
        seconds = kwargs.get('time', 10)
        self.calculation_time = datetime.timedelta(seconds=seconds)

        self.max_moves = kwargs.get('max_moves', 10)

        self.wins = {}
        self.plays = {}

        self.C = kwargs.get('C', 1.4)

        self.use_point = kwargs.get('use_point', True)

    def update(self, state):
        pass

    def get_play(self, state, player):
        self.max_depth = 0
        legal = state.getPossiblePositionList(player)

        if not legal:
            return
        elif len(legal) == 1:
            return (None, legal[0])

        games = 0
        begin = datetime.datetime.utcnow()
        while datetime.datetime.utcnow() - begin < self.calculation_time:
            self.run_simulation(state, player)
            games += 1

        moves_states = []
        for p in legal:
            copy_state = copy.deepcopy(state)
            copy_state.setMarker(player, p)
            moves_states.append((p, copy_state))

        #print games, datetime.datetime.utcnow() - begin

        percent_wins, play_count, move = max(
            (self.wins.get((player, S.getCompressedBoardStr()), 0) /
             self.plays.get((player, S.getCompressedBoardStr()), 1),
             self.plays.get((player, S.getCompressedBoardStr()), 0),
             p)
            for p, S in moves_states
        )

##        for x in sorted(
##            ((100 * self.wins.get((player, S.getCompressedBoardStr()), 0) /
##              self.plays.get((player, S.getCompressedBoardStr()), 1),
##              self.wins.get((player, S.getCompressedBoardStr()), 0),
##              self.plays.get((player, S.getCompressedBoardStr()), 0), p)
##             for p, S in moves_states),
##            reverse=True
##        ):
##            print "{3}: {0: .2f}% ({1} / {2})".format(*x)
##
##        print "Maximum depth searched:", self.max_depth

        return (percent_wins, play_count, move)

    def run_simulation(self, state, player):
        visited_states = set()

        expand = True
        for t in xrange(1, self.max_moves + 1):
            legal = state.getPossiblePositionList(player)

            if legal == []:
                break
            
            moves_states = []
            for p in legal:
                copy_state = copy.deepcopy(state)
                copy_state.setMarker(player, p)
                moves_states.append((p, copy_state))

            if all(self.plays.get((player, S.getCompressedBoardStr())) for p, S in moves_states):
                log_total = math.log(
                    sum(self.plays[(player, S.getCompressedBoardStr())] for p, S in moves_states))
                value, move, state = max(
                    ((self.wins[(player, S.getCompressedBoardStr())] / self.plays[(player, S.getCompressedBoardStr())]) +
                     self.C * math.sqrt(log_total / self.plays[(player, S.getCompressedBoardStr())]), p, S)
                    for p, S in moves_states
                )
            else:
                move, state = random.choice(moves_states)

            if expand and (player, state.getCompressedBoardStr()) not in self.plays:
                expand = False
                self.plays[(player, state.getCompressedBoardStr())] = 0
                self.wins[(player, state.getCompressedBoardStr())] = 0
                if t > self.max_depth:
                    self.max_depth = t

            visited_states.add((player, state))

            player = state.getNextPlayer()
            winner = state.isWin()
            if winner:
                break
        
        for player, state in visited_states:
            if (player, state.getCompressedBoardStr()) not in self.plays:
                continue
            self.plays[(player, state.getCompressedBoardStr())] += 1
            if player == winner or winner == DRAW \
            or (self.use_point and (state.getPoint(state.FIRST) > state.getPoint(state.SECOND)) and player == state.FIRST) \
            or (self.use_point and (state.getPoint(state.FIRST) < state.getPoint(state.SECOND)) and player == state.SECOND):
                self.wins[(player, state.getCompressedBoardStr())] += 1


def saveObject(obj, fileName):
    with open(fileName, "wb") as f:
        pickle.dump(obj, f)


def loadObject(fileName):
    with open(fileName, "rb") as f:
        return pickle.load(f)
