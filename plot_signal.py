import numpy as np
import matplotlib.pyplot as plt

def plot_signal(raw, raw_freq, lfp, lfp_freq, spk, spk_freq, condition='Move'):
    # create three subplots: one for the raw signal, one for the LFP, and one for the spikes
    # each subplot is the signal's voltage as a function of time
    # the time should be in seconds, and according to the sampling frequency of the signal

    # plot
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    # set title for the whole figure
    fig.suptitle(f'Raw, LFP, and Spike Signals in {condition} condition')
    # create time vectors
    raw_time = np.arange(0, len(raw)/raw_freq, 1/raw_freq)
    lfp_time = np.arange(0, len(lfp)/lfp_freq, 1/lfp_freq)
    spk_time = np.arange(0, len(spk)/spk_freq, 1/spk_freq)
    # plot
    ax1.plot(raw_time, raw)
    ax1.set_title('Raw Signal')
    ax2.plot(lfp_time, lfp)
    ax2.set_title('Local Field Potential')
    ax3.plot(spk_time, spk)
    ax3.set_title('Spikes')
    ax3.set_xlabel('Time (s)')
    # y labels in microvolts
    ax1.set_ylabel('Voltage (uV)')
    ax2.set_ylabel('Voltage (uV)')
    ax3.set_ylabel('Voltage (uV)')
    # show
    plt.show()



