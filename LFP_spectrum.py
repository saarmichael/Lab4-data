import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def LFP_spectrum(LFP_signal, sampling_rate):

    # Compute the power spectrum
    f, Pxx = signal.welch(LFP_signal, sampling_rate, window='hann', nperseg=600, noverlap=0.25 * 600, nfft=8192, scaling='density')

    # Plot the power spectrum in dB
    plt.semilogy(f, 10 * np.log10(Pxx))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power (dB)')
    plt.title('Power spectrum of the LFP signal')
    plt.xlim(0, 120)
    plt.show()


    # Compute the spectrogram
    f, t, Sxx = signal.spectrogram(LFP_signal, sampling_rate, nperseg=600, noverlap=0.25 * 600, nfft=8192, scaling='density')

    # Plot the spectrogram
    plt.pcolormesh(t, f, 10 * np.log10(Sxx))  # Convert power to dB
    plt.colorbar(label='Intensity (dB)')  # Add a colorbar
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectrogram of the LFP signal')
    plt.show()