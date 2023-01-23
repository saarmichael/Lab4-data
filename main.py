from plot_signal import plot_signal

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
condition = 'Still'
plot_signal(raw_still[:int(raw_still_freq/12)], raw_still_freq, lfp_still[:int(lfp_still_freq/12)], lfp_still_freq, spk_still[:int(spk_still_freq/12)], spk_still_freq, condition=condition)
condition = 'Move'
plot_signal(raw_move[:int(raw_move_freq/12)], raw_move_freq, lfp_move[:int(lfp_move_freq/12)], lfp_move_freq, spk_move[:int(spk_move_freq/12)], spk_move_freq, condition=condition)