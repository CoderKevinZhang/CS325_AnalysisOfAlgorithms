#under construction by Alec Z.
from statistics import *
from math import sqrt
import sys
import time
import copy

start_Time = time.time()


def main():
    PointArray, PointPairs, minPoints = ([] for i in range(3))
    buildArray(PointArray, PointPairs)
    PointPairsY = copy.deepcopy(PointPairs)
    PointPairsY.sort(key=lambda y: y[1])
    Absolute_Smallest = getSmallestDistance(
        PointPairs, PointPairsY, len(PointPairs), minPoints)
    PaperWork(minPoints, Absolute_Smallest)


def PaperWork(minPoints, Absolute_Smallest):
    End_Time = abs(start_Time - time.time())
    minPoints.sort()
    i = 0
    # This only runs with example.input, strange little bug
    for i in range(len(minPoints)):
        j = i + 1
        while j <= len(minPoints) - 1:
            if minPoints[i] == minPoints[j]:
                del minPoints[i]
                j -= 1
            j += 1
    timeLog = open("timeLog.EnhancedDnC.txt", "a")
    timeLog.write(str(End_Time))
    timeLog.write("\n")
    timeLog.close()
    TieLog = open("Output.EnhancedDnC.txt", "a")
    TieLog.write(str(Absolute_Smallest) + "\n")
    for i in minPoints:
        TieLog.write(str(i) + "\n")
    TieLog.write("\n")
    TieLog.close()


def getSmallestDistance(PointPairs, PointPairsY, nElements, minPoints):

    if (nElements <= 3):
        return BruteForce(PointPairs, minPoints)

    midPoint = int(nElements / 2)
    middleValue = PointPairs[midPoint]
    
    #split points in the y array along the vertical line
    Pyl, Pyr = ([] for i in range(2))
    for i in PointPairsY:
        if (i[0] <= middleValue[0]):
            Pyl.append(i)
        else:
            Pyr.append(i)

    LeftSmallestDist = getSmallestDistance(
        PointPairs[:midPoint], Pyl, midPoint, minPoints)  # Break into left half
    RightSmalestDist = getSmallestDistance(
        PointPairs[midPoint:], Pyr, nElements - midPoint, minPoints)  # Break into right half

    shortest_Dist_In_Halfs = min(LeftSmallestDist, RightSmalestDist)

    Points_Inside_Strip = []

    for i in PointPairsY:
        if (int(i[0] - middleValue[0]) < shortest_Dist_In_Halfs):
            # if the x values differences are smaller than shortest distances in each
            # respective section
            Points_Inside_Strip.append(i)

    return (min(shortest_Dist_In_Halfs, pruneWithMiddle(Points_Inside_Strip, shortest_Dist_In_Halfs, minPoints)))


def getDistance(Point_x1, Point_y1, Point_x2, Point_y2):
    return sqrt(((Point_x2 - Point_x1) ** 2) + ((Point_y2 - Point_y1) ** 2))


def pruneWithMiddle(ShortPoints, minimum, minPoints):
    #ShortPoints.sort(key=lambda x: x[1])  # Sort by the y Coordinate
    for i in range(len(ShortPoints) - 1):
        j = i + 1
        first_Test = ShortPoints[j][1]
        Second_Test = ShortPoints[i][1]
        Y_Value_Dist = first_Test - Second_Test
        while(Y_Value_Dist <= minimum and (j < len(ShortPoints))):
            dist_From_Midpoint = getDistance(ShortPoints[i][0], ShortPoints[i][
                1], ShortPoints[j][0], ShortPoints[j][1])
            Smaller_Dist = min(dist_From_Midpoint, minimum)

            # Check to see if the point is smaller than the distance of the
            # current points
            if (Smaller_Dist < getDistance(minPoints[0][0][0], minPoints[0][0][1], minPoints[0][1][0], minPoints[0][1][1])):
                del minPoints[:]
                minimum = Smaller_Dist
                minPoints.append([ShortPoints[i], ShortPoints[j]])
            # Check to see if the point is equal to the distance of current
            # points
            elif (dist_From_Midpoint == getDistance(minPoints[0][0][0], minPoints[0][0][1], minPoints[0][1][0], minPoints[0][1][1])):
                minPoints.append([ShortPoints[i], ShortPoints[j]])

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
    
    # Make a copy of the array
    # Sorts array of pairs by the second value
    #PointPairsY.sort(key=lambda y: y[1])

def BruteForce(PointArray, minPoints):
    minimum = getDistance(PointArray[1][0], PointArray[0][
        0], PointArray[1][1], PointArray[0][1])
    i = 0
    while(i + 2 <= len(PointArray)):
        j = i + 1
        while (j + 1 <= len(PointArray)):
            dist = getDistance(PointArray[i][0], PointArray[i][1],
                               PointArray[j][0], PointArray[j][1])
            if (dist < minimum):
                minimum = dist
                del minPoints[:]
                minPoints.append([PointArray[i], PointArray[j]])

            j += 1
        i += 1
    return minimum


main()
