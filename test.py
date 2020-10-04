import matplotlib.pyplot as plt
import numpy as np


np.random.seed(0)

dt = 0.01  # sampling interval
Fs = 1 / dt  # sampling frequency
t = np.arange(0, 10, dt)

# generate noise:
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

s =  np.sin(2 * np.pi * 10 * t) + cnse  # the signal

fig, axes = plt.subplots(2,1)

# plot time signal:
axes[0].set_title("Signal")
axes[0].plot(t, s, color='C0')
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Amplitude")

# plot different spectrum types:
axes[1].set_title("Magnitude Spectrum")
axes[1].magnitude_spectrum(s, Fs=Fs, color='C1')


fig.tight_layout()
plt.show()