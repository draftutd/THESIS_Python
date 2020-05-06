import pandas as pd
Time = []
Data = []
dataframe = pd.read_excel (r'Data.xlsx')
i =0 
while i < 16384:
    Time.append(dataframe['Time '][i])
    Data.append(dataframe['g'][i])
    i += 1
    
print(Time)
print(Data)
