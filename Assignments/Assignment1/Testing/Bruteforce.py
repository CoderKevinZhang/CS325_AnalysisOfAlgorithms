from math import sqrt
import sys
import time
start_Time = time.time()


def main():
    PointArray = []
    buildArray(PointArray)
    BruteForce(PointArray)


def buildArray(PointArray):
    openFile = open(sys.argv[1], "r+")
    value = openFile.read().split()
    for i in value:
        if i != ' ' and i != '\n':  # only accept things that are not a space or new line
            PointArray.append(int(i))


def getDistance(Point_x1, Point_y1, Point_x2, Point_y2):
    return sqrt(((Point_x2 - Point_x1) ** 2) + ((Point_y2 - Point_y1) ** 2))


def BruteForce(PointArray):

    minimum = getDistance(PointArray[0], PointArray[
                          1], PointArray[2], PointArray[3])
    i = 4
    minPoints = []
    while(i + 4 <= len(PointArray)):
        j = i + 2
        while (j + 2 <= len(PointArray)):
            # If the new set of points is less than the current minimum,
            # overwrite the minimum

            if ((getDistance(PointArray[i], PointArray[i + 1],
                             PointArray[j], PointArray[j + 1])) < minimum):
                minimum = getDistance(PointArray[i], PointArray[i + 1],
                                      PointArray[j], PointArray[j + 1])
                # delete the previous list if new minimum is found
                del minPoints[:]
                minPoints.append(minimum)  # add the new minimum distance
                # add the points of the minimum distance
                minPoints.append([[PointArray[i], PointArray[
                                 i + 1]], [PointArray[j], PointArray[j + 1]]])

            # If there is a tie between the minimum and the new points output
            # it to a file
            elif ((getDistance(PointArray[i], PointArray[i + 1],
                               PointArray[j], PointArray[j + 1])) == minimum):
                # add the points that tie with the minimum
                minPoints.append([[PointArray[i], PointArray[
                                 i + 1]], [PointArray[j], PointArray[j + 1]]])

            j += 2
        i += 2

    print(minimum)
    timelog = open("timelog_bruteforce.txt", "a")
    current_Time = abs(start_Time - time.time())
    timelog.write(str(current_Time))
    timelog.write("\n")
    timelog.close()

    writeTie = open("output_bruteforce.txt", "a")
    for i in minPoints:
        writeTie.write(str(i))
        writeTie.write('\n')


main()
