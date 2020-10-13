import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
import numpy as np

Data1=[]
data2=[]
data3=[]
figure, axis = plt.subplots(3, 1)
plt.subplots_adjust(hspace=1)
window = np.hanning(8192)
sRate = 8192 # sample rate in Hertz
amplitude1 = 10 # amplitude of first wave
freq1 = 25.0 # frequency of first sine wave
numPeriods = 1 # number of periods of the sine waves
numSamples = sRate * numPeriods # total number of samples
samplingFrequency   = sRate;
x = np.linspace(0, numPeriods, numSamples)
f1 = lambda x: amplitude1*np.sin(freq1*2*np.pi*x)
y = [f1(i) for i in x]

axis[0].plot(window)
axis[0].set_title("Hann window")
axis[0].set_ylabel("Amplitude")
axis[0].set_xlabel("Sample")

for v, y in zip(y, window):
    vaa = v*y
    Data1.append(vaa)
# Time domain representation of the resultant sine wave
axis[1].plot(x, Data1)
axis[1].set_title('Sine wave 25Hz + Hann window')
axis[1].set_xlabel('Time [sec]')
axis[1].set_ylabel('Amplitude [arbitrary]')

# Frequency domain representation
fourierTransform = np.fft.fft(Data1)/len(Data1)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(Data1)/2))] # Exclude sampling frequency
tpCount     = len(Data1)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

absfourierTransform = abs(fourierTransform)*2
for u,i in zip(frequencies,absfourierTransform):
    if u<500:
        data2.append(u)
        data3.append(i)
        
# Frequency domain representation
axis[2].set_title('Fourier transform')
axis[2].plot(data2, data3)
axis[2].set_xlabel('Frequency')
axis[2].set_ylabel('Amplitude')

for x, y in zip(data2,data3 ):
    if y>1.5:
         print(x,y)
         
plt.show()
