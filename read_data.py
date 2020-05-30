import pandas as pd
import matplotlib.pyplot as plt 
Time = []
Data = []
dataframe = pd.read_excel (r'Data.xlsx')
i =0 
while i < 16384:
    Time.append(dataframe['Time '][i])
    Data.append(dataframe['g'][i])
    i += 1
    
x = Time 
y = Data
print(len(y))
plt.plot(x, y)   
plt.xlabel('TIME') 
plt.ylabel('G') 
plt.title('Time domain') 
plt.show() 

