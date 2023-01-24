import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import scipy.io as sio

def firingRate(spike_times, sampling_rate, recording_time):
    # spike_times is a vector of spike times in seconds
    # sampling_rate is the sampling rate of the signal in Hz
    # recording_time is the length of the recording in seconds
    # firing_rate is the firing rate of the neuron in Hz
    # calculate the firing rate of the neuron, using spike train and non-overlapping windows
    # the window size is 0.1 seconds
    window_size = 0.1
    # calculate the number of windows
    num_windows = int(recording_time/window_size)
    # calculate the number of spikes in each window
    spike_counts = np.zeros(num_windows)
    for i in range(num_windows):
        # get the start and end of the window
        start = i*window_size
        end = (i+1)*window_size
        # get the number of spikes in the window
        spike_counts[i] = np.sum((spike_times>=start) & (spike_times<end))
    # calculate the firing rate
    firing_rate = spike_counts/window_size

    # plot the firing rate
    plt.figure()
    plt.plot(np.arange(num_windows)*window_size, firing_rate)
    plt.xlabel('time (s)')
    plt.ylabel('firing rate (Hz)')
    plt.title('Firing rate of the neuron')
    plt.show()

    return firing_rate

