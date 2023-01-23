import numpy as np
import matplotlib.pyplot as plt

def spike_detection(signal, freq):
    # function that detects spikes in a signal and returns an array of the times of the spikes
    # the signal is a 1D array of voltage values

    # define threshold and minISI
    threshold = -50 # in microvolts
    minISI = 4 # in ms

    # find the times of the spikes (the spikes are negative, BELOW the threshold)
    # the spikes are the points where the signal crosses the threshold
    spike_times = []
    spike_values = []
    # iterate over the signal (from index 1 to the end) and check if signal[i] < threshold and signal[i-1] > threshold
    i = 1
    while i < len(signal):
        if signal[i] < threshold and signal[i-1] > threshold:
            spike_times.append(i)
            spike_values.append(signal[i])
            i += int((minISI*freq)/1000) # skip the next minISI ms
        else:
            i += 1
    
    # convert spike_times to seconds
    spike_times = np.array(spike_times)/freq
    time = np.arange(0, len(signal)/freq, 1/freq)
    # plot the signal and scatter the spike times
    plt.plot(time, signal, color='black')
    plt.scatter(spike_times, spike_values, color='red')
    plt.show()
    return spike_times
