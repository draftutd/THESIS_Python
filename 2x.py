import numpy as np
import matplotlib.pyplot as plt

sRate = 1000 # sample rate in Hertz
amplitude1 = 10 # amplitude of first wave
amplitude2 = 5 # amplitude of second wave
freq1 = 150.0 # frequency of first sine wave
freq2 = 160.0 # frequency of second sine wave
numPeriods = 1 # number of periods of the sine waves
numSamples = sRate * numPeriods # total number of samples

samplingFrequency   = sRate;
figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)

x = np.linspace(0, numPeriods, numSamples)
f1 = lambda x: amplitude1*np.sin(freq1*2*np.pi*x)
f2 = lambda x: amplitude2*np.sin(freq2*2*np.pi*x)
y = [(f1(i)+f2(i)) for i in x]

# Time domain representation of the resultant sine wave
axis[0].plot(x, y)
axis[0].set_title('Sine wave 150Hz + Sine wave 160Hz')
axis[0].set_xlabel('Time [sec]')
axis[0].set_ylabel('Amplitude [arbitrary]')

# Frequency domain representation
fourierTransform = np.fft.fft(y)/len(y)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(y)/2))] # Exclude sampling frequency
tpCount     = len(y)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

# Frequency domain representation
axis[1].set_title('Fourier transform depicting the frequency components')
axis[1].plot(frequencies, abs(fourierTransform))
axis[1].set_xlabel('Frequency')
axis[1].set_ylabel('Amplitude')
plt.show() 
