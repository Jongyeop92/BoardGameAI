# -*- coding: utf8 -*-

import sys
sys.path.append("../GameAI")

from GameAI import *
from OtheloBoard import *

import time


def main():
    
    state = OtheloBoard(8, 8, BLACK, WHITE)
    maxPlayer = False

    monteCarlo = MonteCarlo(time=3, max_moves=100)

    minTime = None
    maxTime = None
    totalTime = 0
    count = 0

    human = input()

    if human in [0, 1]:
        human = human == 0

    while True:

        marker = state.getNextPlayer()
        maxPlayer = not maxPlayer

        print "Black:", state.blackCount
        print "White:", state.whiteCount
        state.showBoard()

        result = state.isWin()

        if result != None:
            break
        elif state.getPossiblePositionList(marker) == []:
            if state.lastMarker == marker:
                break
        else:
            if human == maxPlayer:
                while True:
                    print "input:",
                    y, x = map(int, raw_input().split())
                    
                    if state.setMarker(marker, (y, x)):
                        break

                    print marker
                    print "Wrong position"
            else:
                start = time.time()

                if marker == BLACK:
                    info = monteCarlo.get_play(state, marker)
                    #info = minimax(state, 3, maxPlayer, True)
                    #info = alphabeta(state, 5, -INFINITE, INFINITE, maxPlayer, True)
                    pass
                else:
                    #info = monteCarlo.get_play(state, marker)
                    info = minimax(state, 3, maxPlayer, True)
                    pass
                
                #info = minimax(state, 3, maxPlayer, True)
                #info = alphabeta(state, 3, -INFINITE, INFINITE, maxPlayer, True)
                #info = monteCarlo.get_play(state, nowColor)
                
                gap = time.time() - start

                if minTime == None or gap < minTime:
                    minTime = gap

                if maxTime == None or gap > maxTime:
                    maxTime = gap

                totalTime += gap
                count += 1

                state.setMarker(marker, info[-1])

                print marker
                print "Info:", info
                print "Gap :", gap
                
        print


    print "Win:", state.isWin()
    print "Black:", state.blackCount
    print "White:", state.whiteCount
    print
    print "MinTime  :", minTime
    print "MaxTime  :", maxTime
    print "MeanTime :", (totalTime / count)
    print "TotalTime:", totalTime
    print
    print "Count:", count


if __name__ == "__main__":
    main()
