import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
samplingFrequency   = 8000;
figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)
Time = []
Data = []
velocity = []
dataframe = pd.read_excel (r'Data.xlsx')
i =0 
while i < 16384:
    Time.append(dataframe['Time '][i])
    Data.append(dataframe['g'][i])
    i += 1

# Time domain representation of the resultant sine wave
axis[0].plot(Time, Data)   
axis[0].set_xlabel('TIME') 
axis[0].set_ylabel('G') 
axis[0].set_title('Time domain')

# Frequency domain representation
fourierTransform = np.fft.fft(Data)/len(Data)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(Data)/2))] # Exclude sampling frequency
tpCount     = len(Data)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency

frequencies = values/timePeriod


for x, y in zip(frequencies, abs(fourierTransform)):
            if(x>=2 and x<=1000):
                        velocity1=(y*9806.65)/(2*np.pi*x)
            else:
                        velocity1=0
            velocity.append(velocity1)

# Frequency domain representation
axis[1].set_title('Fourier transform depicting the frequency components')
axis[1].plot(frequencies, velocity)
axis[1].set_xlabel('Frequency')
axis[1].set_ylabel('Amplitude')
plt.show() 
