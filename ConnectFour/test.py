# -*- coding: utf8 -*-

import sys
sys.path.append("../GameAI")

from ConnectFourBoard import *
from GameAI import *


def test():

    state = ConnectFourBoard(7, 6)

    assert state.getBoard() == [[EMPTY] * 7] * 6
    assert state.getPossiblePositionList(None) == [0, 1, 2, 3, 4, 5, 6]
    assert state.isWin() == None

    state.setMarker(RED, 0)
    assert state.getBoard() == [[EMPTY] * 7] * 5 + \
                               [[RED, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]
    assert state.getPossiblePositionList(BLUE) == [0, 1, 2, 3, 4, 5, 6]
    assert state.getNextPlayer() == BLUE

    state.setMarker(BLUE, 1)
    assert state.getBoard() == [[EMPTY] * 7] * 5 + \
                               [[RED, BLUE, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]]
    assert state.getNextPlayer() == RED
    assert state.isFull() == False

    state.setMarker(RED, 0)
    state.setMarker(RED, 0)
    state.setMarker(RED, 0)
    assert state.isWin() == RED

    for x in range(7):
        for y in range(6):
            state.setMarker(BLUE, x)

    assert state.isFull() == True
    assert state.getPossiblePositionList(RED) == []
    assert state.isWin() == BLUE


    print "Success"


if __name__ == "__main__":
    test()
