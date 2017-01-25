import matplotlib.pyplot as plt
import sys
plt.figure()

PointArray = []
openFile = open(sys.argv[1], "r+")
value = openFile.read()
time_Values = value.split()
i = 0
for i in range(len(time_Values)):
    time_Values[i] = float(time_Values[i])
# create some data
inputSize = [10, 100, 1000, 10000, 100000]
# plot the two lines
#plt.axis([10, 100000, 0, 200])
plt.plot(inputSize, time_Values, 'ro-')

plt.savefig("Test.pdf")
