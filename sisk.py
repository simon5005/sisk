#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#col_list = ["Leftover Capture Data"]
col_list = ["HID Data"]
data = pd.read_csv("sisk.csv",usecols=col_list)
#byte = data['Leftover Capture Data']
byte = data['HID Data']

x =[None] * len(byte)
y =[None] * len(byte)
x[0] = 0
y[0] = 0
x_dis =[None] * len(byte)
y_dis =[None] * len(byte)
b0 = [None] * len(byte)
b1 =[None] * len(byte)
b2 =[None] * len(byte)


for i in range(len(byte)):
    b0[i] = int(byte[i][2:4], 16)
    b1[i] = int(byte[i][4:6], 16)
    b2[i]= int(byte[i][6:8], 16)
    x[0] = b1[0]
    y[0] = b2[0]
  
    
    if b0[i] == 0 :
        print(i,": Pressed Nothing")
    elif b0[i] == 1:
        print(i,": Pressed LBM")
    elif b0[i] ==2:
        print(i,": Pressed RBM")
    elif b0[i] ==3:
        print(i,": Pressed LBM+RBM")
    else:
        print(i,": Pressed Wheel")
          # byte1: X displacement
    x_dis[i]  = b1[i]
    if x_dis[i] >127:
        x_dis[i] = x_dis[i]- 255


        # byte2: Y displacement
    y_dis[i] = b2[i]
    if y_dis[i] > 127:
        y_dis[i] = y_dis[i] - 255

    if i < 1 :
        x[i] =x[0]+ (x_dis[i])
        y[i] =y[0]+ (y_dis[i])
    else:
        x[i] =x[i-1]+ (x_dis[i])
        y[i] =y[i-1]+ (y_dis[i])
 

def Convert(lst):
    lst = np.array(lst)
    return list(-lst)

y = Convert(y)
plt.plot(x,y)
plt.show()
