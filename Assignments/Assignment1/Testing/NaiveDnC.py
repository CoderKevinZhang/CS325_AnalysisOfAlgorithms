from statistics import *
from math import sqrt
import sys
import time

start_Time = time.time()


def main():
    PointArray = []
    PointPairs = []

    buildArray(PointArray, PointPairs)
    Absolute_Smallest = getSmallestDistance(PointPairs, len(PointPairs))
    print(Absolute_Smallest)
    End_Time = start_Time - time.time()
    timeLog = open("timeLog.NaiveDnC.txt", "a")
    timeLog.write(str(End_Time))
    timeLog.write("\n")
    timeLog.close()


def getSmallestDistance(PointPairs, nElements):

    if (nElements <= 3):
        # print("Inside Base case", PointPairs)
        return BruteForce(PointPairs)

    midPoint = int(nElements / 2)
    middleValue = PointPairs[midPoint]

    LeftSmallestDist = getSmallestDistance(
        PointPairs[:midPoint], midPoint)  # Break into left half
    RightSmalestDist = getSmallestDistance(
        PointPairs[midPoint:], nElements - midPoint)  # Break into right half
    if (RightSmalestDist == 0.0):
        print("fuck by L/R")
    shortest_Dist_In_Half = min(LeftSmallestDist, RightSmalestDist)

    Points_Inside_Strip = []

    for i in PointPairs:
        if (int(i[0] - middleValue[0]) < shortest_Dist_In_Half):
            Points_Inside_Strip.append(i)
    if (shortest_Dist_In_Half == 0.0):
        print("fuck")
    return (pruneWithMiddle(Points_Inside_Strip, shortest_Dist_In_Half))


def getDistance(Point_x1, Point_y1, Point_x2, Point_y2):
    return sqrt(((Point_x2 - Point_x1) ** 2) + ((Point_y2 - Point_y1) ** 2))


def pruneWithMiddle(ShortPoints, minimum):
    ShortPoints.sort(key=lambda x: x[1])  # Sort by the y Coordinate
    for i in range(len(ShortPoints) - 1):
        j = i + 1
        first_Test = ShortPoints[j][1]
        Second_Test = ShortPoints[i][1]
        Some_Number = first_Test - Second_Test
        while((Some_Number) <= minimum and (j <= len(ShortPoints) - 1)):
            dist_From_Midpoint = getDistance(ShortPoints[j][0], ShortPoints[j][
                1], ShortPoints[i][0], ShortPoints[i][1])
            Test_Min = min(dist_From_Midpoint, minimum)
            if (Test_Min == 0.0 or minimum == 0.0):
                print("Fuck in pruner")
            if (Test_Min < minimum):
                minimum = Test_Min
            j += 1

    return minimum


def buildArray(PointArray, PointPairs):
    openFile = open(sys.argv[1], "r+")
    value = openFile.read().split()

    for i in value:
        if i != ' ' and i != '\n':  # only accept things that are not a space or new line
            PointArray.append(int(i))
    i = 0
    while i + 2 <= len(PointArray):
        PointPairs.append([PointArray[i], PointArray[i + 1]])
        i += 2
    # Sorts array of pairs by the first value (xCoordinates)
    PointPairs.sort(key=lambda x: x[0])


def BruteForce(PointArray):
    #print("Inside BruteForce")
    # print(PointArray)
    minimum = getDistance(PointArray[1][0], PointArray[0][
                          0], PointArray[1][1], PointArray[0][1])
    i = 0
    while(i + 2 <= len(PointArray)):
        j = i + 1
        while (j + 1 <= len(PointArray)):
            if ((getDistance(PointArray[i][0], PointArray[i][1],
                             PointArray[j][0], PointArray[j][1])) < minimum):
                minimum = getDistance(PointArray[i][0], PointArray[i][1],
                                      PointArray[j][0], PointArray[j][1])
            j += 1
        i += 1
    if (minimum == 0.0):
        print("Fuck in BruteForce")
    return minimum


main()
