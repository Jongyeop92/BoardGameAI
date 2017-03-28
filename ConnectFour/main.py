# -*- coding: utf8 -*-

import sys
sys.path.append("../GameAI")

from GameAI import *
from ConnectFourBoard import *

import time


def main():

    state = ConnectFourBoard(7, 6)
    maxPlayer = False

    monteCarlo = MonteCarlo(time=5, max_moves=100)

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
                x = input()

                if state.setMarker(marker, x):
                    break

                print marker
                print "Wrong position"
        else:
            start = time.time()

            if marker == RED:
                info = monteCarlo.get_play(state, marker)
                pass
            else:
                info = monteCarlo.get_play(state, marker)
                pass

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
