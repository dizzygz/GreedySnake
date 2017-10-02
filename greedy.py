#!/bin/python3

import sys
from enum import Enum


class DirecNum(Enum):
    NOTMOVE = '#'
    EAST = 'e'
    SOUTH = 's'
    WEAST = 'w'
    NORTH = 'n'


class MoveCel:
    dicCel = {}
    winDirec = DirecNum.NOTMOVE
    curDirect = DirecNum.NOTMOVE

    def windEastMove(curCel):
        nextCol = curCel.col
        nextRow = curCel.row
        if MoveCel.winDirec == DirecNum.EAST:
            if MoveCel.curDirect == DirecNum.NOTMOVE or MoveCel.curDirect == DirecNum.EAST:
                nextCol = curCel.col + 1
                MoveCel.curDirect = DirecNum.EAST
                if nextCol > curCel.maxLine - 1:
                    nextCol = curCel.maxLine - 1
                    if (nextRow + 1, nextCol) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow + 1, nextCol)].getVisit() == False:
                        MoveCel.curDirect = DirecNum.SOUTH
                        nextRow += 1
                    else:
                        MoveCel.curDirect = DirecNum.NORTH
                        nextRow -= 1

            elif MoveCel.curDirect == DirecNum.NORTH:
                nextRow = curCel.row - 1
                if nextRow < 0 or MoveCel.dicCel[(nextRow, nextCol)].getVisit() == True:
                    nextRow += 1
                    if (nextRow, nextCol - 1) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow, nextCol - 1)].getVisit() == False:
                        MoveCel.curDirect = DirecNum.WEAST
                        nextCol -= 1


            elif MoveCel.curDirect == DirecNum.SOUTH:
                nextRow = curCel.row + 1
                if nextRow > curCel.maxLine - 1 or MoveCel.dicCel[(nextRow, nextCol)].getVisit() == True:
                    nextRow -= 1
                    if (nextRow, nextCol - 1) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow, nextCol - 1)].getVisit() == False:
                        MoveCel.curDirect = DirecNum.WEAST
                        nextCol -= 1
            else:
                if (curCel.row + 1, curCel.col) in MoveCel.dicCel and MoveCel.dicCel[
                    (curCel.row + 1, curCel.col)].getVisit() == False:
                    nextRow = curCel.row + 1
                    MoveCel.curDirect = DirecNum.SOUTH
                else:
                    nextRow = curCel.row - 1
                    MoveCel.curDirect = DirecNum.NORTH

        return nextRow, nextCol

    def windWeastMove(curCel):
        nextCol = curCel.col
        nextRow = curCel.row
        if MoveCel.winDirec == DirecNum.WEAST:
            if MoveCel.curDirect == DirecNum.NOTMOVE or MoveCel.curDirect == DirecNum.WEAST:
                nextCol = curCel.col -1
                MoveCel.curDirect = DirecNum.WEAST
                if nextCol < 0:
                    nextCol = 0
                    if (nextRow + 1, nextCol) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow + 1, nextCol)].getVisit() == False:
                        MoveCel.curDirect = DirecNum.SOUTH
                        nextRow += 1
                    else:
                        MoveCel.curDirect = DirecNum.NORTH
                        nextRow -= 1

            elif MoveCel.curDirect == DirecNum.NORTH:
                nextRow = curCel.row - 1
                if nextRow < 0 or MoveCel.dicCel[(nextRow, nextCol)].getVisit() == True:
                    nextRow += 1
                    if (nextRow, nextCol + 1) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow, nextCol + 1)].getVisit() == False:
                        MoveCel.curDirect = DirecNum.EAST
                        nextCol += 1


            elif MoveCel.curDirect == DirecNum.SOUTH:
                nextRow = curCel.row + 1
                if nextRow > curCel.maxLine - 1 or MoveCel.dicCel[(nextRow, nextCol)].getVisit() == True:
                    nextRow -= 1
                    if (nextRow, nextCol + 1) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow, nextCol + 1)].getVisit() == False:
                        MoveCel.curDirect = DirecNum.EAST
                        nextCol += 1
            else: # move east
                if (curCel.row + 1, curCel.col) in MoveCel.dicCel and MoveCel.dicCel[
                    (curCel.row + 1, curCel.col)].getVisit() == False:
                    nextRow = curCel.row + 1
                    MoveCel.curDirect = DirecNum.SOUTH
                else:
                    nextRow = curCel.row - 1
                    MoveCel.curDirect = DirecNum.NORTH

        return nextRow, nextCol

    def windNorthMove(curCel):
        nextCol = curCel.col
        nextRow = curCel.row
        if MoveCel.winDirec == DirecNum.NORTH:
            if MoveCel.curDirect == DirecNum.NOTMOVE or MoveCel.curDirect == DirecNum.NORTH:
                nextRow = curCel.row -1
                MoveCel.curDirect = DirecNum.NORTH
                if nextRow < 0:
                    nextRow = 0
                    if (nextRow , nextCol+1) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow, nextCol+1)].getVisit() == False:
                        MoveCel.curDirect = DirecNum.EAST
                        nextCol += 1
                    else:
                        MoveCel.curDirect = DirecNum.WEAST
                        nextCol -= 1

            elif MoveCel.curDirect == DirecNum.WEAST:
                nextCol = curCel.col - 1
                if nextCol < 0 or MoveCel.dicCel[(nextRow, nextCol)].getVisit() == True:
                    nextCol += 1
                    if (nextRow+1, nextCol ) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow+1, nextCol )].getVisit() == False:
                        MoveCel.curDirect = DirecNum.SOUTH
                        nextRow += 1


            elif MoveCel.curDirect == DirecNum.EAST:
                nextCol = curCel.col + 1
                if nextCol > curCel.maxLine - 1 or MoveCel.dicCel[(nextRow, nextCol)].getVisit() == True:
                    nextCol -= 1
                    if (nextRow+1, nextCol ) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow+1, nextCol )].getVisit() == False:
                        MoveCel.curDirect = DirecNum.SOUTH
                        nextRow += 1
            else: # move south
                if (curCel.row, curCel.col+1) in MoveCel.dicCel and MoveCel.dicCel[
                    (curCel.row , curCel.col+1)].getVisit() == False:
                    nextCol = curCel.col + 1
                    MoveCel.curDirect = DirecNum.EAST
                else:
                    nextCol = curCel.col - 1
                    MoveCel.curDirect = DirecNum.WEAST

        return nextRow, nextCol

    def windSouthMove(curCel):
        nextCol = curCel.col
        nextRow = curCel.row
        if MoveCel.winDirec == DirecNum.SOUTH:
            if MoveCel.curDirect == DirecNum.NOTMOVE or MoveCel.curDirect == DirecNum.SOUTH:
                nextRow = curCel.row +1
                MoveCel.curDirect = DirecNum.SOUTH
                if nextRow > curCel.maxLine - 1:
                    nextRow = curCel.maxLine - 1
                    if (nextRow , nextCol+1) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow, nextCol+1)].getVisit() == False:
                        MoveCel.curDirect = DirecNum.EAST
                        nextCol += 1
                    else:
                        MoveCel.curDirect = DirecNum.WEAST
                        nextCol -= 1

            elif MoveCel.curDirect == DirecNum.WEAST:
                nextCol = curCel.col - 1
                if nextCol < 0 or MoveCel.dicCel[(nextRow, nextCol)].getVisit() == True:
                    nextCol += 1
                    if (nextRow-1, nextCol ) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow-1, nextCol )].getVisit() == False:
                        MoveCel.curDirect = DirecNum.NORTH
                        nextRow -= 1


            elif MoveCel.curDirect == DirecNum.EAST:
                nextCol = curCel.col + 1
                if nextCol > curCel.maxLine - 1 or MoveCel.dicCel[(nextRow, nextCol)].getVisit() == True:
                    nextCol -= 1
                    if (nextRow-1, nextCol ) in MoveCel.dicCel and MoveCel.dicCel[
                        (nextRow-1, nextCol )].getVisit() == False:
                        MoveCel.curDirect = DirecNum.NORTH
                        nextRow -= 1
            else: # move north
                if (curCel.row, curCel.col+1) in MoveCel.dicCel and MoveCel.dicCel[
                    (curCel.row , curCel.col+1)].getVisit() == False:
                    nextCol = curCel.col + 1
                    MoveCel.curDirect = DirecNum.EAST
                else:
                    nextCol = curCel.col - 1
                    MoveCel.curDirect = DirecNum.WEAST

        return nextRow, nextCol

    def getNext(curCel):
        MoveCel.dicCel[(curCel.row,curCel.col)].setVisit()

        if MoveCel.winDirec == DirecNum.EAST:
            return MoveCel.windEastMove(curCel)

        if MoveCel.winDirec == DirecNum.NORTH:
            return MoveCel.windNorthMove(curCel)

        if MoveCel.winDirec == DirecNum.WEAST:
            return MoveCel.windWeastMove(curCel)

        if MoveCel.winDirec == DirecNum.SOUTH:
            return MoveCel.windSouthMove(curCel)


class Cel:
    def __init__(self, iX, iY, N):
        self.row = iX
        self.col = iY
        self.maxLine = N
        self.visited = False

    def setVisit(self):
        self.visited = True

    def getVisit(self):
        return self.visited

    def findNexRow(iCol):
        if self.row + 1 in range(self.maxLine) and dicCel[(self.row + 1, iCol)].visited == False:
            return self.row + 1


if __name__ == "__main__":
    n = int(input().strip())
    d = input().strip()
    x, y = input().strip().split(' ')
    x, y = [int(x), int(y)]
    # Write Your Code Here
    matrix = [[0 for col in range(n)] for row in range(n)]
    runed = False;

    for i in range(n):
        for j in range(n):
            MoveCel.dicCel[(i, j)] = Cel(i, j, n)

    MoveCel.curDirect = DirecNum.NOTMOVE
    MoveCel.winDirec = DirecNum.EAST if d == 'e' else MoveCel.winDirec
    MoveCel.winDirec = DirecNum.SOUTH if d == 's' else MoveCel.winDirec
    MoveCel.winDirec = DirecNum.NORTH if d == 'n' else MoveCel.winDirec
    MoveCel.winDirec = DirecNum.WEAST if d == 'w' else MoveCel.winDirec

    currentCel = Cel(x,y,n)
    time =1
    for i in range(n):
        for j in range(n):
            matrix[currentCel.row][currentCel.col] = time
            time +=1
            if time > n*n:
                break;
            irow, icol = MoveCel.getNext(currentCel)
            currentCel = MoveCel.dicCel[irow,icol]


    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print('')



