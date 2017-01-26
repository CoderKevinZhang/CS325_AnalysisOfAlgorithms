import matplotlib.pyplot as plt
import sys
import numpy as np

plt.figure()

PointArray = []
openFile = open(sys.argv[1], "r+")
value = openFile.read()
time_Values = value.split()
i = 0

for i in range(len(time_Values)):
    time_Values[i] = float(time_Values[i])

print(time_Values)

# create some data
inputSize = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
# plot the two lines
#plt.axis([10, 100000, 0, 200])
plt.plot(inputSize, time_Values, "ro-")
plt.ylabel('Time (Seconds)')
plt.xlabel('Input size')
plt.title(sys.argv[1])
PDF_File = sys.argv[1][:-3] + "pdf"
plt.savefig(PDF_File)
