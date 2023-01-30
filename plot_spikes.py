import numpy as np
import matplotlib.pyplot as plt

def plot_spikes(signal, spike_times, freq, window_size=0.002):
    # function that plots all the windows around the spikes
    # the signal is a 1D array of voltage values
    # the spike_times is an array of the times of the spikes

    step = int(window_size*freq/2)
    window_time = np.arange(-window_size/2, window_size/2, 1/freq)
    windows = []
    fig = plt.figure()
    fig.suptitle(f'{window_size*1000} ms windows around spikes')
    # subplot 1
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title('All windows with the average spike +1 std')

    for i in range(len(spike_times)):
        # get the time of the spike
        spike_time = spike_times[i]
        # get the index of the spike
        spike_index = int(spike_time*freq)
        # get the window around the spike
        window = signal[spike_index-step:spike_index+step]
        # append the window to the list of windows
        if len(window) == len(window_time):
            windows.append(window)
            # generate random color for the window
            color = np.random.rand(3,)
            # plot the window
            # check if the window is the same size as the window_time
            ax1.plot(window_time, window, color=color, linewidth=1)
    # show

    # calculate the average window and one standard deviation
    windows = np.array(windows)
    avg_window = np.mean(windows, axis=0)
    std_window = np.std(windows, axis=0)
    # plot the average window and one standard deviation
    ax1.plot(window_time, avg_window, color='black', linewidth=4)
    ax1.fill_between(window_time, avg_window-std_window, avg_window+std_window, color='grey', alpha=0.3)
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('voltage (uV)')
    # add text to the plot with the average spike amplitude and the std
    ax1.text(0.15, 0.20, f'avg spike peak: {np.max(avg_window):.2f} uV', transform=ax1.transAxes, fontsize=10, verticalalignment='bottom')
    ax1.text(0.15, 0.15, f'spikes peak std: {np.max(std_window):.2f} uV', transform=ax1.transAxes, fontsize=10, verticalalignment='bottom')

    
    # collect three points from each window and plot them on a 3D plot
    # each axis represents a point in the window
    sample_points = []
    for w in windows:
        # find the maximum value
        max_value = np.max(w)
        min_value = np.min(w)
        max_index = np.where(w==max_value)[0][0]
        min_index = np.where(w==min_value)[0][0]
        # find the the max value that is after the minimum value
        max_value_after_min = np.max(w[min_index:])
        sample_points.append((max_value, min_value, max_value_after_min))
        
        max_after_min_index = np.where(w==max_value_after_min)[0][0]
        # plot the points
        ax1.scatter(window_time[max_index], max_value, color='red', edgecolors='black', alpha=0.5)
        ax1.scatter(window_time[min_index], min_value, color='red', edgecolors='black', alpha=0.5)
        ax1.scatter(window_time[max_after_min_index], max_value_after_min, color='red', edgecolors='black', alpha=0.5, s=20)
    sample_points = np.array(sample_points)
    # scatter the sample_points on the plot
    # second subplot
    # scatter the points in small size
    # plot the points in 3D in small size and with border around them
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.set_title('3D scatter of three measurements from each window')
    ax2.scatter(sample_points[:, 0], sample_points[:, 1], sample_points[:, 2], color='red', edgecolors='black', alpha=0.5)
    # add labels to the axes
    ax2.set_xlabel('max value (uV)')
    ax2.set_ylabel('min value (uV)')
    ax2.set_zlabel('max value after min (uV)')
    

    plt.show()
    return None