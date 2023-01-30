from min_ISI import min_ISI
from plot_signal import plot_signal
from spike_detection import spike_detection
from plot_spikes import plot_spikes

# import the data from .mat files
import scipy.io as sio
raw_still           = sio.loadmat('CWB_Still.mat')['StillWB'][0]
raw_still_freq      = sio.loadmat('CWB_Still.mat')['sampling_freq'][0][0]
raw_move            = sio.loadmat('CWB_Move.mat')['MoveWB'][0]
raw_move_freq       = sio.loadmat('CWB_Move.mat')['sampling_freq'][0][0]
lfp_still           = sio.loadmat('CLFP_Still.mat')['LFPStill'][0]
lfp_still_freq      = sio.loadmat('CLFP_Still.mat')['sampling_freq'][0][0]
lfp_move            = sio.loadmat('CLFP_Move.mat')['LFPMove'][0]
lfp_move_freq       = sio.loadmat('CLFP_Move.mat')['sampling_freq'][0][0]
spk_still           = sio.loadmat('CSPK_Still.mat')['StillSPK'][0]
spk_still_freq      = sio.loadmat('CSPK_Still.mat')['sampling_freq'][0][0]
spk_move            = sio.loadmat('CSPK_Move.mat')['MoveSPK'][0]
spk_move_freq       = sio.loadmat('CSPK_Move.mat')['sampling_freq'][0][0]

# plot the move signals
# plot_signal(raw_move, raw_move_freq, lfp_move, lfp_move_freq, spk_move, spk_move_freq)
# plot only the first 10th of a second of the still signals
divider = 1
condition = 'Still'
# plot_signal(raw_still[:int(raw_still_freq/divider)], raw_still_freq, lfp_still[:int(lfp_still_freq/divider)], lfp_still_freq, spk_still[:int(spk_still_freq/divider)], spk_still_freq, condition=condition)
# plot_signal(raw_move[:int(raw_move_freq/divider)], raw_move_freq, lfp_move[:int(lfp_move_freq/divider)], lfp_move_freq, spk_move[:int(spk_move_freq/divider)], spk_move_freq)


# detect spikes in the still signals
detected = spike_detection(spk_move[3*int(spk_move_freq/divider):4*int(spk_move_freq/divider)], spk_move_freq, True, 'Move')
#plot_spikes( spk_move, detected, freq = spk_move_freq)
detected = spike_detection(spk_still[3*int(spk_still_freq/divider):4*int(spk_still_freq/divider)], spk_still_freq, True, 'Still')
#plot_spikes( spk_still, detected, freq = spk_still_freq)