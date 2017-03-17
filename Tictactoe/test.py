# -*- coding: utf8 -*-

from Board import *
from MonteCarlo import *

import copy

def test():
    
    state = Board(3, 3)

    assert state.getBoard() == [[EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY],
                                [EMPTY, EMPTY, EMPTY]]
    
    assert state.getPossiblePositionList() == [(0, 0), (0, 1), (0, 2),
                                               (1, 0), (1, 1), (1, 2),
                                               (2, 0), (2, 1), (2, 2)]

    assert state.isWin() == None

    state.setMark(X_MARK, (0, 0))

    assert state.getBoard() == [[X_MARK, EMPTY, EMPTY],
                                [ EMPTY, EMPTY, EMPTY],
                                [ EMPTY, EMPTY, EMPTY]]

    assert state.getPossiblePositionList() == [        (0, 1), (0, 2),
                                               (1, 0), (1, 1), (1, 2),
                                               (2, 0), (2, 1), (2, 2)]

    #state.showBoard()
    

    state.setMark(O_MARK, (2, 1))

    assert state.getBoard() == [[X_MARK,  EMPTY, EMPTY],
                                [ EMPTY,  EMPTY, EMPTY],
                                [ EMPTY, O_MARK, EMPTY]]

    assert state.getPossiblePositionList() == [        (0, 1), (0, 2),
                                               (1, 0), (1, 1), (1, 2),
                                               (2, 0),         (2, 2)]

    #state.showBoard()

    assert state.isFull() == False

    for y in range(3):
        for x in range(3):
            state.setMark(X_MARK, (y, x))

    assert state.isFull() == True
    assert state.getPossiblePositionList() == []
    assert state.isWin() == X_MARK


    assert state.isInBoard(0, 0) ==  True
    assert state.isInBoard(2, 2) ==  True
    assert state.isInBoard(3, 3) == False

    newState = copy.deepcopy(state)
    assert id(state) != id(newState)
    assert id(state.getBoard()) != id(newState.getBoard())


    monteCarlo = MonteCarlo(time=5)
    state = Board(3, 3)

    print monteCarlo.get_play(state, X_MARK)
    print
    

    print "Success"


if __name__ == "__main__":
    test()
