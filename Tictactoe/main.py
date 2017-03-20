# -*- coding: utf8 -*-

import sys
sys.path.append("../GameAI")

from GameAI import *
from TictactoeBoard import *

import time


def main():
    state = TictactoeBoard(3, 3, X_MARK, O_MARK)
    maxPlayer = False

    monteCarlo = MonteCarlo(time=5, max_moves=10)

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
        
        state.showBoard()

        if state.isWin():
            break

        if human == maxPlayer:
            while True:
                y, x = map(int, raw_input().split())

                if state.setMarker(marker, (y, x)):
                    break

                print marker
                print "Wrong position"
        else:
            start = time.time()

            if marker == X_MARK:
                info = monteCarlo.get_play(state, marker)
                pass
            else:
                info = minimax(state, 10, maxPlayer, True)
                #info = alphabeta(state, 9, -INFINITE, INFINITE, maxPlayer, True)
                pass

            #info = minimax(state, 9, maxPlayer, True)
            #info = alphabeta(state, 9, -INFINITE, INFINITE, maxPlayer, True)
            #info = monteCarlo.get_play(state, marker)

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
    print
    print "MinTime  :", minTime
    print "MaxTime  :", maxTime
    print "MeanTime :", (totalTime / count)
    print "TotalTime:", totalTime
    print
    print "Count:", count


if __name__ == "__main__":
    main()
