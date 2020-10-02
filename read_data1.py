import pandas as pd
Time = []
Data = []

def read_data():
    dataframe = pd.read_excel (r'Data1.xlsx')
    i =0 
    while i < 6400:
        Time.append(dataframe['Time '][i]*60)
        Data.append(dataframe['g'][i])
        i += 1
    return Time,Data

