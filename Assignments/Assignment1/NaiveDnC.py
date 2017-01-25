from statistics import *
from math import sqrt


def main():
    PointArray = []
    PointPairs = []

    buildArray(PointArray, PointPairs)
    getSmallestDistance(PointPairs, len(PointPairs))


def getSmallestDistance(PointPairs, nElements):

    if (nElements <= 3):
        #print("Inside Base case", PointPairs)
        return BruteForce(PointPairs)

    midPoint = int(nElements / 2)
    middleValue = PointPairs[midPoint]

    LeftSmallestDist = getSmallestDistance(
        PointPairs[:midPoint], midPoint)  # Break into left half
    RightSmalestDist = getSmallestDistance(
        PointPairs[midPoint:], nElements - midPoint)  # Break into right half

    shortest_Dist_In_Half = min(LeftSmallestDist, RightSmalestDist)

    Points_Inside_Strip = []
    # print(PointPairs, middleValue[0])
    for i in PointPairs:
        if (int(i[0] - middleValue[0]) < shortest_Dist_In_Half):
            Points_Inside_Strip.append(i)
        print(Points_Inside_Strip)

    return (pruneWithMiddle(Points_Inside_Strip, shortest_Dist_In_Half))


def getDistance(Point_x1, Point_y1, Point_x2, Point_y2):
    return sqrt(((Point_x2 - Point_x1) ** 2) + ((Point_y2 - Point_y1) ** 2))


def pruneWithMiddle(ShortPoints, minimum):
    print("I am the points inside the strip", ShortPoints)
    smallest = BruteForce(ShortPoints)
    if smallest < minimum:
        return smallest

    print("I'm the smallest value", smallest, minimum)
    return minimum


def buildArray(PointArray, PointPairs):
    openFile = open("example.input", "r+")
    value = openFile.read()
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
    print("Inside BruteForce")
    print(PointArray)
    minimum = getDistance(PointArray[1][0], PointArray[0][
                          0], PointArray[1][1], PointArray[1][1])
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

    return minimum


main()

    """
    xCoordinates = []
    for i in PointPairs:
        xCoordinates.append(i[0])  # Goes through each pair and grabs x value

    print(xCoordinates)
    divider = int(median(xCoordinates))
    print("The median is ", int(median(xCoordinates)))
    leftArray = []
    rightArray = []
    for i in PointPairs:
        if (i[0] < divider):
            leftArray.append(i)
        else:
            rightArray.append(i)

    print(leftArray)  # used for later.. I think
    print(rightArray)
"""
