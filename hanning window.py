import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
import numpy as np

window = np.hanning(3200)
print(len(window))
print(window)
plt.plot(window)
plt.title("Hann window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.figure()

A = fft(window, 2048) / 25.5
mag = np.abs(fftshift(A))
freq = np.linspace(-0.5, 0.5, len(A))
with np.errstate(divide='ignore', invalid='ignore'):
    response = 20 * np.log10(mag)
response = np.clip(response, -100, 100)

print(len(freq))
print(freq)
print(len(response))
print(response)
#plt.plot(freq, response)
#plt.title("Frequency response of the Hann window")
#plt.ylabel("Magnitude [dB]")
#plt.xlabel("Normalized frequency [cycles per sample]")
#plt.axis('tight')

plt.show()
