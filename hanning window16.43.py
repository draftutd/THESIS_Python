import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def export(x,y):
     f = open('datalog.txt', 'a')
     f.write('%s\t%s\n'%(x,y))
     f.close()

window = np.hanning(16384)
samplingFrequency   = 8192; #คูณ2.56เท่า
figure, axis = plt.subplots(3, 1)
plt.subplots_adjust(hspace=1)
Time = []
Data = []
Data1 = []
dataframe = pd.read_excel (r'Data2.xlsx')
i =0
while i < 16384:
    Time.append(dataframe['Time '][i])
    Data.append(dataframe['g'][i])
    i += 1
    
# Time domain representation of the resultant sine wave
axis[0].plot(Time,Data)   
axis[0].set_xlabel('TIME') 
axis[0].set_ylabel('G') 
axis[0].set_title('Time domain')

for x, y in zip(Data, window):
    vaa = x*y
    Data1.append(vaa)
    
axis[1].plot(Time,Data1)   
axis[1].set_xlabel('TIME') 
axis[1].set_ylabel('G') 
axis[1].set_title('hanning window')

# Frequency domain representation
fourierTransform = np.fft.fft(Data1)/len(Data1)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(Data1)/2))] # Exclude sampling frequency
tpCount     = len(Data1)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

# Frequency domain representation
axis[2].set_title('Fourier transform depicting the frequency components')
axis[2].plot(frequencies, abs(fourierTransform)*2.2477)
axis[2].set_xlabel('Frequency')
axis[2].set_ylabel('Amplitude')

for x, y in zip(frequencies, abs(fourierTransform)*2.2477):
    export(x,y)
plt.show()
