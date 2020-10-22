import lvm_read
import numpy as np
import matplotlib.pyplot as plt
import urllib
rte = 3200
time =[]
x1 =[]
x2 =[]
x3 =[]
filename = '123.lvm'
lvm = lvm_read.read(filename, read_from_pickle=False)
lvm.keys()

u = 0
while u < rte:
    time.append(lvm[0]['data'][u][0])
    u += 1
            

i = len(lvm[0]['data'])-rte
while i < len(lvm[0]['data']):
    x1.append(lvm[0]['data'][i][1])
    x2.append(lvm[0]['data'][i][2])
    x3.append(lvm[0]['data'][i][3]) 
    i += 1

