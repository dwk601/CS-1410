# imports of libraries
import glob
import numpy as np
import matplotlib.pyplot as plt

# Constant variables
VT = 100
WIDTH = 50

# Making smooth data array


def smooth(data):
    res = data.copy()

    for n in range(3, len(data) - 3):
        res[n] = (data[n - 3] + 2 * data[n - 2] + 3 * data[n - 1] + 3 *
                  data[n] + 3 * data[n + 1] + 2 * data[n + 2] + data[n + 3]) // 15

    return res

# analyze the data


def analyze(filename):

    rawData = np.loadtxt(filename)

    smoothData = smooth(rawData)

    pulses = []
    i = 0

    while i < len(smoothData) - 2:
        if smoothData[i + 2] - smoothData[i] > VT:
            pulses.append(i)

            i += 1
            while i < len(smoothData) - 2 and smoothData[i + 1] > smoothData[i]:
                i += 1
        i += 1
    if not pulses:
        return

    outputString = f'{filename}:\n'
    for i in range(len(pulses)):
        startPos = pulses[i]
        realWidth = WIDTH

        if i < len(pulses) - 1 and pulses[i] + realWidth > pulses[i + 1]:
            realWidth = pulses[i + 1] - startPos
        realWidth = min(realWidth, len(smoothData) - startPos)
        area = int(sum(rawData[startPos:startPos + realWidth]))
        outputString += f'Pulse {i + 1}: {startPos + 1} ({area})\n'

# open the out file
    with open(filename[:-3] + "out", "w") as outfile:
        print(outputString, file=outfile, end="")

# Plot the data
    _, axes = plt.subplots(nrows=2)
    axes[0].plot(rawData, linewidth=.2)
    axes[0].set(title=filename, ylabel="raw")
    axes[1].plot(smoothData, linewidth=.3)
    axes[1].set(ylabel="smooth")
# plt.show()
    plt.savefig(filename[:-3] + "pdf")


def main():

    for fname in glob.glob("*.dat"):
        analyze(fname)


if __name__ == "__main__":
    main()
