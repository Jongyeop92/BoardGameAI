# -*- coding: utf8 -*-

from OtheloBoard import *

def test():

    state = OtheloBoard(8, 8)

    assert state.getBoard() == [[EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY, EMPTY, EMPTY, WHITE, BLACK, EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY] * 8]

    assert state.blackCount == 2
    assert state.whiteCount == 2

    assert state.isInBoard(0, 0)   == True
    assert state.isInBoard(4, 4)   == True
    assert state.isInBoard(8, 8)   == False
    assert state.isInBoard(-1, -1) == False

    assert state.getPossiblePositionList(BLACK)  == [(2, 3), (3, 2), (4, 5), (5, 4)]
    assert state.getPossiblePositionList(WHITE) == [(2, 4), (3, 5), (4, 2), (5, 3)]

    assert state.isValidPosition(BLACK, (2, 3)) == True
    assert state.isValidPosition(BLACK, (0, 0)) == False
    assert state.isValidPosition(WHITE, (2, 4)) == True
    assert state.isValidPosition(WHITE, (1, 1)) == False

    assert state.setMarker(BLACK, (1, 1)) == False
    assert state.setMarker(BLACK, (2, 3)) == True
    assert state.getBoard() == [[EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY, EMPTY, EMPTY,  BLACK,        EMPTY, EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY,  BLACK,  BLACK, EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY,  BLACK, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY] * 8]

    assert state.blackCount == 4
    assert state.whiteCount == 1
    assert state.getPossiblePositionList(WHITE) == [(2, 2), (2, 4), (4, 2)]

    assert state.setMarker(WHITE, (0, 0)) == False
    assert state.setMarker(WHITE, (2, 4)) == True
    assert state.getBoard() == [[EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],
                                [EMPTY] * 8,
                                [EMPTY] * 8,
                                [EMPTY] * 8]

    assert state.blackCount == 3
    assert state.whiteCount == 3
    assert state.getPossiblePositionList(BLACK) == [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]

    assert state.isWin() == None

    assert state.getBoardStr() == ("-" * 8    + "\n" +
                                   "-" * 8    + "\n" +
                                   "---BW---" + "\n" +
                                   "---BW---" + "\n" +
                                   "---BW---" + "\n" +
                                   "-" * 8    + "\n" +
                                   "-" * 8    + "\n" +
                                   "-" * 8)
                                  

    state.showBoard()

    
    print "Success"


if __name__ == "__main__":
    test()
