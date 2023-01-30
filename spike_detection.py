import numpy as np
import matplotlib.pyplot as plt

def spike_detection(signal, freq, to_plot=False, condition='Move'):
    # function that detects spikes in a signal and returns an array of the times of the spikes
    # the signal is a 1D array of voltage values
    # calculate the std of the signal
    std = np.std(signal)
    # define threshold and minISI
    threshold = -1.5*std
    minISI = 3 # in ms

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
    # for each spike time find the peak that comes after it
    peaks = []
    peaks_values = []
    for i in range(len(spike_times)):
        j = int(spike_times[i]*freq)
        flag = True
        while flag:
            if signal[j] > signal[j+1]:
                j += 1
            else:
                peaks.append(j)
                peaks_values.append(signal[j])
                flag = False
    # convert peaks to seconds
    peaks = np.array(peaks)/freq
        
    time = np.arange(0, len(signal)/freq, 1/freq)
    # plot the signal and scatter the spike times
    if to_plot:
        # make sure that the scatter points are on top of the line
        # add title and axes titles
        plt.title(f'Spike Detection for {condition} condition')
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (uV)')
        #plt.scatter(spike_times, spike_values, color='red')
        color = '#505154'
        plt.scatter(peaks, peaks_values, color='blue', zorder=1, s=10)
        plt.plot(time, signal, color=color, alpha=1, zorder=-1)
        plt.show()
    return spike_times
