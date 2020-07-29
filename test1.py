import numpy as np
import matplotlib.pyplot as plt 

fs = 300 # sample rate 
f = 100 # the frequency of the signal

samplingFrequency   = fs;
figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)

x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
y = np.sin(2*np.pi*f * (x/fs))


# Time domain representation of the resultant sine wave
axis[0].plot(x, y)   
axis[0].set_xlabel('sample rate') 
axis[0].set_ylabel('sine wave') 
axis[0].set_title('Time domain')

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
