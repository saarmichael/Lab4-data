import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from spike_detection import spike_detection

def min_ISI(signal, freq):
    # calculate the ISI histogram and plot it
    # the signal is a 1D array of voltage values
    # the freq is the sampling frequency of the signal
    # the function returns the minimum ISI
    ISI = []
    spike_times = spike_detection(signal, freq)
    for i in range(len(spike_times)-1):
        ISI.append(spike_times[i+1]-spike_times[i]) 
    
    # plot the ISI histogram
    plt.hist(ISI, bins=200)
    plt.show()
