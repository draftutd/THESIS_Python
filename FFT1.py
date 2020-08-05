import read_data1
import numpy as np
import matplotlib.pyplot as plt 

Time,Data = read_data1.read_data()

samplingFrequency   = 400000;
figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)

x = Time 
y = Data

# Time domain representation of the resultant sine wave
axis[0].plot(x, y)   
axis[0].set_xlabel('TIME') 
axis[0].set_ylabel('G') 
axis[0].set_title('Time domain')


plt.show() 
