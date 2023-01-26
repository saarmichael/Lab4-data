from plot_signal import plot_signal
from spike_detection import spike_detection
from plot_spikes import plot_spikes
from Firing_rate import firingRate
from LFP_spectrum import LFP_spectrum

# import the data from .mat files
import scipy.io as sio

# raw signal
raw_still           = sio.loadmat('CWB_Still.mat')['StillWB'][0]
raw_still_freq      = sio.loadmat('CWB_Still.mat')['sampling_freq'][0][0]
raw_move            = sio.loadmat('CWB_Move.mat')['MoveWB'][0]
raw_move_freq       = sio.loadmat('CWB_Move.mat')['sampling_freq'][0][0]

# lfp signal
lfp_still           = sio.loadmat('CLFP_Still.mat')['LFPStill'][0]
lfp_still_freq      = sio.loadmat('CLFP_Still.mat')['sampling_freq'][0][0]
lfp_move            = sio.loadmat('CLFP_Move.mat')['LFPMove'][0]
lfp_move_freq       = sio.loadmat('CLFP_Move.mat')['sampling_freq'][0][0]

# spike signal
spk_still           = sio.loadmat('CSPK_Still.mat')['StillSPK'][0]
spk_still_freq      = sio.loadmat('CSPK_Still.mat')['sampling_freq'][0][0]
spk_move            = sio.loadmat('CSPK_Move.mat')['MoveSPK'][0]
spk_move_freq       = sio.loadmat('CSPK_Move.mat')['sampling_freq'][0][0]

# plot only the first 10th of a second of the still signals
divider = 0.5

# function 1:
condition = 'Still'
plot_signal(raw_still[:int(raw_still_freq/divider)], raw_still_freq, lfp_still[:int(lfp_still_freq/divider)], lfp_still_freq, spk_still[:int(spk_still_freq/divider)], spk_still_freq, condition=condition)
condition = 'Move'
plot_signal(raw_move[:int(raw_move_freq/divider)], raw_move_freq, lfp_move[:int(lfp_move_freq/divider)], lfp_move_freq, spk_move[:int(spk_move_freq/divider)], spk_move_freq, condition=condition)

# function 2:
# detect spikes in the still signals
detected = spike_detection(spk_move[:int(spk_move_freq/divider)], spk_move_freq, False)

# BONUS function 2:
plot_spikes(spk_move[:int(spk_move_freq/divider)], detected, freq=spk_move_freq)

# function 3:
# calculate and plot the firing rate of the neuron in each time window
firing_rate = firingRate(detected, spk_move_freq, len(spk_move[:int(spk_move_freq/divider)])/spk_move_freq)

# function 4:
# LFP spectrum analysis
LFP_spectrum(lfp_move, lfp_move_freq)