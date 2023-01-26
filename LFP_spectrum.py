import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

def LFP_spectrum(SPK_signal, sampling_rate):

    # plot SPK signal spectrum and signal spectogram
    f, Pxx = welch(SPK_signal, sampling_rate, nperseg=600, noverlap=600 * 0.25, nfft=8192)
    plt.figure()
    plt.plot(f, Pxx)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power')
    plt.title('Power spectrum of SPK signal')
    plt.show()

    # plot the signal spectogram
    plt.figure()
    plt.specgram(SPK_signal, NFFT=8192, Fs=sampling_rate)
    plt.xlabel('time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectogram of SPK signal')
    plt.show()

    return f, Pxx