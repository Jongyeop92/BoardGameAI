# -*- coding: utf8 -*-

import sys
sys.path.append("../Board")

from Board import *


RED  = 'O'
BLUE = 'X'


class ConnectFourBoard(Board):

    def __init__(self, width, height, FIRST=RED, SECOND=BLUE):
        Board.__init__(self, width, height, FIRST, SECOND)

        self.WIN_COUNT = 4

    def getPoint(self, marker):
        point = 0

        for y in range(self.height):
            for x in range(self.width):

                if self.board[y][x] != marker: continue

                maxSameMarkCount = 0
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

                    if sameMarkCount > maxSameMarkCount:
                        maxSameMarkCount = sameMarkCount

                if maxSameMarkCount >= self.WIN_COUNT:
                    point = INFINITE
                    break
                else:
                    point += maxSameMarkCount

            if point == INFINITE:
                break

        return point

    def getPossiblePositionList(self, marker):
        possiblePositionList = []

        for x in range(self.width):
            if self.board[0][x] == EMPTY:
                possiblePositionList.append(x)

        return possiblePositionList

    def setMarker(self, marker, position):
        if self.board[0][position] == EMPTY:

            y = self.height - 1
            while self.board[y][position] != EMPTY:
                y -= 1

            self.board[y][position] = marker
            self.lastPosition = (y, position)
            self.lastMarker = marker
            
            return True

        return False

    def getNextPlayer(self):
        if self.lastMarker == None or self.lastMarker == self.SECOND:
            return self.FIRST
        else:
            return self.SECOND

    def isFull(self):
        for x in range(self.width):
            if self.board[0][x] == EMPTY:
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

            if sameMarkCount >= self.WIN_COUNT:
                return marker

        if self.isFull():
            return DRAW

        return None
