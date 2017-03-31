# -*- coding: utf8 -*-

EMPTY  = '-'

DRAW = "DRAW"

INFINITE = 999999999

class Board:

    def __init__(self, width, height, FIRST='F', SECOND='S'):
        self.width = width
        self.height = height
        self.board = self.makeBoard(width, height)
        self.FIRST = FIRST
        self.SECOND = SECOND
        self.lastPosition = None
        self.lastMarker = None
        self.directionPairList = [[(-1, 0), ( 1,  0)],
                                  [(-1, 1), ( 1, -1)],
                                  [( 0, 1), ( 0, -1)],
                                  [( 1, 1), (-1, -1)]]

    def makeBoard(self, width, height):
        board = []

        for i in range(height):
            board.append([EMPTY] * width)

        return board
    
    def getBoard(self):
        return self.board

    def getBoardStr(self):
        return '\n'.join(''.join(row) for row in self.board)

    def getCompressedBoardStr(self):
        boardStr = self.getBoardStr().replace('\n', '')

        compressedBoardStr = ''

        ch = boardStr[0]
        count = 1
        for i in range(1, len(boardStr)):
            if ch == boardStr[i]:
                count += 1
            else:
                if count > 1 or ch == EMPTY:
                    compressedBoardStr += str(count) + ch
                else:
                    compressedBoardStr += ch

                ch = boardStr[i]
                count = 1

        compressedBoardStr += str(count) + ch

        return compressedBoardStr.replace(EMPTY, '')

    def showBoard(self):
        for row in self.board:
            print '+'.join(row)
        print

    def getNextPlayer(self):
        return None

    def getPossiblePositionList(self, marker):
        return []

    def setMarker(self, marker, position):
        return False

    def isValidPosition(self, marker, position):
        return position in self.getPossiblePositionList(marker)

    def getPoint(self, marker):
        return 0

    def isWin(self):
        return None

    def isInBoard(self, y, x):
        return 0 <= y and y < self.height and 0 <= x and x < self.width

    def getMaxPlayer(self, maxPlayer):
        if maxPlayer:
            return self.FIRST
        else:
            return self.SECOND
