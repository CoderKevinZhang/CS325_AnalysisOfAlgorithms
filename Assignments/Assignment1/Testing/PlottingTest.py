import matplotlib.pyplot as plt

plt.figure()

PointArray = []
openFile = open("10^1.txt", "r+")
value = openFile.read()
test = value.split()

j = 0
print(test)
while (j + 1 <= len(test)):
    PointArray.append([int(test[j]), int(test[j + 1])])
    j = j + 2
print(PointArray)


# create some data
x_series = PointArray
y_series_1 = [x**2 for x in x_series]
y_series_2 = [x**3 for x in x_series]

# plot the two lines
plt.plot(x_series, y_series_1)
plt.plot(x_series, y_series_2)

plt.savefig("Test.pdf")
