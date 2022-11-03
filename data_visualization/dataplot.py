import glob
import numpy as np
import matplotlib.pyplot as plt

#constant variables
vt = 100
width = 50

#smooth data array by averaging
def smooth(data):
    res = data.copy()
    
    for n in range(3, len(data) -3):
        #floor((yi−3+2yi−2+3yi−1+3yi+3yi+1+2yi+2+yi+3)/15)
        res[n] = np.floor((data[n-3] + 2*data[n-2] + 3*data[n-1] + 3*data[n] + 3*data[n+1] + 2*data[n+2] + data[n+3])/15)

    return res

#analyze data file
def analyze(filename):
    raw_data = np.loadtxt(filename, dtype=np.int32)
    
    smooth_data = smooth(raw_data)
    
    pulses = []
    i = 0
    
    while i < len(smooth_data) - 2:
        if smooth_data[i+2] -smooth_data[i] > vt:
            pulses.append(i)
            i += width
            while i < len(smooth_data) - 2 and smooth_data[i+1] > smooth_data[i]:
                i += 1
        i += 1
    if not pulses:
        print("No pulse found in file", filename)
        return
    
    output_str = f"{filename}:\n"
    for i in range(len(pulses)):
        start_pos = pulses[i]
        real_width = width
        
        if i < len(pulses) - 1 and pulses[i] + real_width > pulses[i+1]:
            real_width = pulses[i+1] - start_pos
        real_width = min(real_width, len(smooth_data) - start_pos)
        area = np.sum(raw_data[start_pos:start_pos+real_width])
        output_str += f"pulse {i+1} at {start_pos + 1} with area {area}\n"
        
    #open the output file
    with open(filename[:-3] + "out", "w") as output_file:
        print(output_str, file=output_file, end="")
        
        #plot the data
        _, ax = plt.subplots(nrows=2)
        ax[0].plot(raw_data, label="raw data", linewidth=0.2)
        ax[0].set(title= filename, ylabel="raw data")
        ax[1].plot(smooth_data, label="smooth data", linewidth=0.3)
        ax[1].set(ylabel="smooth data")
        #plt.show()
        plt.savefig(filename[:-3] + "pdf")



def main():
    for fname in glob.glob("*.dat"):
        analyze(fname)
        
        
if __name__ == "__main__":
    main()