import matplotlib
import numpy as np
import wave, math
from matplotlib import pyplot as plt

# Variables
sRate = 10000 # sample rate in Hertz
freq1 = 50.0 # frequency of first sine wave
freq2 = 100.0 # frequency of second sine wave
amplitude1 = 10 # amplitude of first wave
amplitude2 = 5 # amplitude of second wave
numPeriods = 2 # number of periods of the sine waves
numSamples = sRate * numPeriods # total number of samples

# Graphing helper function
def setup_graph(title='', x_label='', y_label='', fig_size=None):
    fig = plt.figure()
    if fig_size != None:
        fig.set_size_inches(fig_size[0], fig_size[1])
    ax = fig.add_subplot(111)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
# Create the x axis from 0 to numPeriods, divided into numSamples samples.
x = np.linspace(0, numPeriods, numSamples)
f1 = lambda x: amplitude1*np.sin(freq1*2*np.pi*x)
f2 = lambda x: amplitude2*np.sin(freq2*2*np.pi*x)
sampled_f1 = [f1(i) for i in x]
sampled_f2 = [f2(i) for i in x]
sampled_fcomb = [(f1(i)+f2(i)) for i in x]

fig = plt.figure()
fig.set_size_inches(12,6)
plt.subplots_adjust(hspace=1)

plt.subplot(311)
plt.plot(x, sampled_f1)
plt.title('Sine wave 5Hz')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude [arbitrary]')
plt.xlim(0, 0.5)
plt.ylim(-15, 15)
