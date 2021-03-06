import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
samplingFrequency   = 8192; #คูณ2.56เท่า
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


def export(x,y):
     f = open('datalog.txt', 'a')
     f.write('%s\t%s\n'%(x,y))
     f.close()

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
print(frequencies)

for x, y in zip(frequencies, abs(fourierTransform)):
            #print(x)
            if(x>=2 and x<=1000):
                        velocity1=(y*9815)/(2*np.pi*x)
                        #velocity1=velocity1/0.7071067811 #คูณรูท2
            else:
                        velocity1=0
            velocity.append(velocity1)
            export(x,y)

    
# Frequency domain representation
axis[1].set_title('Fourier transform depicting the frequency components')
axis[1].plot(frequencies, abs(fourierTransform))
axis[1].set_xlabel('Frequency')
axis[1].set_ylabel('Amplitude')
plt.show() 

