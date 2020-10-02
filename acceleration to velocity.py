import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
samplingFrequency   = 6400;
figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)
Time = []
Data = []
velocity = [0]
dataframe = pd.read_excel (r'Data.xlsx')
i =0 
while i < 16384:
    Time.append(dataframe['Time '][i])
    Data.append(dataframe['g'][i]*9.8)
    i += 1

# Time domain representation of the resultant sine wave
axis[0].plot(Time, Data)   
axis[0].set_xlabel('TIME') 
axis[0].set_ylabel('G') 
axis[0].set_title('Time domain')

acceleration = Data
time = 0.0001 #10Hz
for acc in acceleration:
    velocity.append(velocity[-1] + acc * time)
del velocity[0]
# Frequency domain representation
fourierTransform = np.fft.fft(velocity)/len(velocity)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(velocity)/2))] # Exclude sampling frequency
tpCount     = len(velocity)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod


# Frequency domain representation
axis[1].set_title('Fourier transform depicting the frequency components')
axis[1].plot(frequencies, abs(fourierTransform))
axis[1].set_xlabel('Frequency')
axis[1].set_ylabel('Amplitude')
plt.show() 
