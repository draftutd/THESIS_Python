import read_data
import numpy as np
import matplotlib.pyplot as plt 

Time,Data = read_data.read_data()

samplingFrequency   = 6400;
figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)

x = Time 
y = Data

# Time domain representation of the resultant sine wave
axis[0].plot(x, y)   
axis[0].set_xlabel('TIME') 
axis[0].set_ylabel('G') 
axis[0].set_title('Time domain')

# Frequency domain representation
fourierTransform = np.fft.fft(Data)/len(Data)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(Data)/2))] # Exclude sampling frequency
tpCount     = len(Data)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = (values/timePeriod)

# Frequency domain representation
axis[1].set_title('Fourier transform depicting the frequency components')
axis[1].plot(frequencies, abs(fourierTransform))
axis[1].set_xlabel('Frequency')
axis[1].set_ylabel('Amplitude')

plt.show() 
