# -*- coding: utf8 -*-

import sys
sys.path.append("../GameAI")

from TictactoeBoard import *
from GameAI import *

import copy

def test():
    
    state = TictactoeBoard(3, 3)

    assert state.getBoard() == [[EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY]]
    
    assert state.getPossiblePositionList(None) == [(0, 0), (0, 1), (0, 2),
                                                   (1, 0), (1, 1), (1, 2),
                                                   (2, 0), (2, 1), (2, 2)]

    assert state.isWin() == None

    state.setMarker(X_MARK, (0, 0))

    assert state.getBoard() == [[X_MARK, EMPTY, EMPTY],
                                [ EMPTY, EMPTY, EMPTY],
                                [ EMPTY, EMPTY, EMPTY]]

    assert state.getPossiblePositionList(O_MARK) == [        (0, 1), (0, 2),
                                                     (1, 0), (1, 1), (1, 2),
                                                     (2, 0), (2, 1), (2, 2)]

    #state.showBoard()
    

    state.setMarker(O_MARK, (2, 1))

    assert state.getBoard() == [[X_MARK,  EMPTY, EMPTY],
                                [ EMPTY,  EMPTY, EMPTY],
                                [ EMPTY, O_MARK, EMPTY]]

    assert state.getPossiblePositionList(X_MARK) == [        (0, 1), (0, 2),
                                                     (1, 0), (1, 1), (1, 2),
                                                     (2, 0),         (2, 2)]

    #state.showBoard()

    assert state.isFull() == False

    for y in range(3):
        for x in range(3):
            state.setMarker(X_MARK, (y, x))

    assert state.isFull() == True
    assert state.getPossiblePositionList(None) == []
    assert state.isWin() == X_MARK


    assert state.isInBoard(0, 0) ==  True
    assert state.isInBoard(2, 2) ==  True
    assert state.isInBoard(3, 3) == False

    newState = copy.deepcopy(state)
    assert id(state) != id(newState)
    assert id(state.getBoard()) != id(newState.getBoard())


##    monteCarlo = MonteCarlo(time=5)
##    state = TictactoeBoard(3, 3)
##
##    print "moteCarlo"
##    print monteCarlo.get_play(state, X_MARK)
##    print
##    print "minimax"
##    print minimax(state, 9, True, True)
##    print
    

    print "Success"


if __name__ == "__main__":
    test()
