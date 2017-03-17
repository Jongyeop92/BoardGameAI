# -*- coding: utf8 --

import sys
sys.path.append("../Board")

from Board import *


X_MARK = 'X'
O_MARK = 'O'


class TictactoeBoard(Board):

    def __init__(self, width, height, FIRST='F', SECOND='S'):
        Board.__init__(self, width, height, FIRST, SECOND)

        self.WIN_COUNT = 3

    def getPossiblePositionList(self, marker):
        possiblePositionList = []

        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == EMPTY:
                    possiblePositionList.append((y, x))

        return possiblePositionList

    def setMarker(self, marker, position):
        y, x = position

        if self.isValidPosition(marker, position):
            self.board[y][x] = marker
            self.lastPosition = position
            self.lastMarker = marker

            return True

        return False

    def getNextPlayer(self):
        if self.lastMarker == None or self.lastMarker == self.SECOND:
            return self.FIRST
        else:
            return self.SECOND

    def isFull(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == EMPTY:
                    return False

        return True
    
    def isWin(self):
        if self.lastPosition == None: return None

        y, x = self.lastPosition
        marker = self.board[y][x]

        for directionPair in self.directionPairList:
            sameMarkCount = 1
            for direction in directionPair:
                dy, dx = direction
                nowY, nowX = y, x

                while self.isInBoard(nowY + dy, nowX + dx):
                    nowY += dy
                    nowX += dx
                    
                    if self.board[nowY][nowX] == marker:
                        sameMarkCount += 1
                    else:
                        break

            if sameMarkCount == self.WIN_COUNT:
                return marker

        if self.isFull():
            return DRAW

        return None
