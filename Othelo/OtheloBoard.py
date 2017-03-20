# -*- coding: utf8 -*-

import sys
sys.path.append("../Board")

from Board import *


BLACK = 'B'
WHITE = 'W'


class OtheloBoard(Board):

    def __init__(self, width, height, FIRST='F', SECOND='S'):
        Board.__init__(self, width, height, FIRST, SECOND)

        self.blackCount = 2
        self.whiteCount = 2

        self.board[height / 2 - 1][width / 2 - 1] = SECOND
        self.board[height / 2 - 1][width / 2    ] = FIRST
        self.board[height / 2    ][width / 2 - 1] = FIRST
        self.board[height / 2    ][width / 2    ] = SECOND

    def getPoint(self, marker):
        if marker == self.FIRST:
            return self.blackCount
        else:
            return self.whiteCount

    def getPossiblePositionList(self, marker):
        possiblePositionList = []

        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == EMPTY:
                    
                    isPossiblePosition = False
                    
                    for directionPair in self.directionPairList:
                        for direction in directionPair:
                            dy, dx = direction
                            nowY, nowX = y, x
                            flipCount = 0

                            while True:
                                nowY += dy
                                nowX += dx

                                if not self.isInBoard(nowY, nowX) or self.board[nowY][nowX] == EMPTY:
                                    flipCount = 0
                                    break
                                elif self.board[nowY][nowX] == marker:
                                    break
                                else:
                                    flipCount += 1

                            if flipCount != 0:
                                possiblePositionList.append((y, x))
                                isPossiblePosition = True
                                break

                        if isPossiblePosition:
                            break

        return possiblePositionList

    def setMarker(self, marker, position):
        if self.isValidPosition(marker, position):
            y, x = position
            self.board[y][x] = marker

            if marker == self.FIRST:
                self.blackCount += 1
            else:
                self.whiteCount += 1

            self.flipMarker(position)
            self.lastPosition = position
            self.lastMarker = marker

            return True
        
        return False

    def flipMarker(self, position):
        y, x = position
        marker = self.board[y][x]

        for directionPair in self.directionPairList:
            for direction in directionPair:
                dy, dx = direction
                nowY, nowX = y, x
                flipPositionList = []

                while True:
                    nowY += dy
                    nowX += dx

                    if not self.isInBoard(nowY, nowX) or self.board[nowY][nowX] == EMPTY:
                        flipPositionList = []
                        break
                    elif self.board[nowY][nowX] == marker:
                        break
                    else:
                        flipPositionList.append((nowY, nowX))

                for flipPosition in flipPositionList:
                    flipY, flipX = flipPosition
                    self.board[flipY][flipX] = marker

                flipCount = len(flipPositionList)
                
                if marker == self.FIRST:
                    self.blackCount += flipCount
                    self.whiteCount -= flipCount
                else:
                    self.blackCount -= flipCount
                    self.whiteCount += flipCount

    def getNextPlayer(self):
        if self.lastMarker == None or self.lastMarker == self.SECOND:
            if self.getPossiblePositionList(self.FIRST) != []:
                return self.FIRST
            else:
                return self.SECOND
        else:
            if self.getPossiblePositionList(self.SECOND) != []:
                return self.SECOND
            else:
                return self.FIRST

    def isWin(self):
        if self.getPossiblePositionList(self.FIRST) == [] and self.getPossiblePositionList(self.SECOND) == []:
            if self.getPoint(self.FIRST) > self.getPoint(self.SECOND):
                return self.FIRST
            elif self.getPoint(self.FIRST) < self.getPoint(self.SECOND):
                return self.SECOND
            else:
                return DRAW
        else:
            return None
