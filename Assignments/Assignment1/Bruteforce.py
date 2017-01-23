from math import sqrt


def main():
    PointArray = []
    buildArray(PointArray)
    print(PointArray)
    BruteForce(PointArray)


def buildArray(PointArray):
    openFile = open("example.input", "r+")
    value = openFile.read()
    for i in value:
        if i != ' ' and i != '\n':
            PointArray.append(int(i))


def getDistance(Point_x1, Point_y1, Point_x2, Point_y2):
    return sqrt(((Point_x2 - Point_x1) ** 2) + ((Point_y2 - Point_y1) ** 2))


def BruteForce(PointArray):
    i = 4
    minimum = getDistance(PointArray[0], PointArray[
                          1], PointArray[2], PointArray[3])
    print(minimum)
    while(i + 4 <= len(PointArray)):
        j = i + 2
        while (j + 2 <= len(PointArray)):
            if ((getDistance(PointArray[i], PointArray[i + 1],
                             PointArray[j], PointArray[j + 1])) < minimum):
                minimum = getDistance(PointArray[i], PointArray[i + 1],
                                      PointArray[j], PointArray[j + 1])
                print(minimum)
            elif ((getDistance(PointArray[i], PointArray[i + 1],
                               PointArray[j], PointArray[j + 1])) == minimum):
                print("TIE!!!")
                print(PointArray[i])
                print(PointArray[i + 1])
                print(PointArray[j])
                print(PointArray[j + 1])

            j += 2
        i += 2
main()
