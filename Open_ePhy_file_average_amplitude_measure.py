# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:34:56 2019

@author: ludov
"""

#First import neo, numpy and pyplot
import neo
import numpy as np
from matplotlib import pyplot as plt

#Open the file with neo 
my_file = neo.io.AxographIO(r"C:\Users\ludov\Downloads\c2, 28-2-2018 006.axgd")

#Create a block object
bl = my_file.read_block()

#Create 2 lists to collect time and signal vectors 
TIME, REC = [],[]

#This loop will append one by one each episode of the recording in our lists
for episode in bl.segments :
    time = episode.analogsignals[0].times #The time vector
    TIME.append(time)
    
    rec = episode.analogsignals[0].magnitude #The signal vector    
    leak = np.mean(rec[0:100]) #The offest of the trace
    REC.append(rec-leak) #We extract the signal minus the offset
    

#Let's compute the average recording 
AVERAGE = np.mean(REC,axis = 0)


#Now it's time the show everything
plt.figure()

#Let's display each trace superimposed
for i in range(len(REC)):
    plt.plot(TIME[i],REC[i],color = '0.5', alpha = 0.4)

#And the the average
plt.plot(TIME[0],AVERAGE,color='blue')



#To find the PSC amplitude, we first have to set our time window for measurement
#Here between 501 and 540 ms 
start = np.ravel(np.where(TIME[0] >= 0.501))[0]
stop = np.ravel(np.where(TIME[0] >= 0.540))[0]

#Now we get the minimum value in the window (=max amp)
#And the index of the value (ie where it is in the global vector)
MIN = np.min(AVERAGE[start:stop])
MIN_idx = TIME[0][np.ravel(np.where(AVERAGE == MIN))[0]]

#And we plot it
plt.scatter(MIN_idx,MIN, s=50, color='orange')

#Add a few graphic element on the plot
plt.xlabel('Time (s)')
plt.ylabel('Signal (Amp)')
plt.title('It is amazing')

#Limits the plot borders for better view
plt.xlim(TIME[0][start],TIME[0][stop])
plt.ylim(-3e-10,0.5e-10)




