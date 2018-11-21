#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First import pandas and numpy
import numpy, pandas


# In[2]:


#Now let's load the data from the excel in the python environnement
data = pandas.read_excel(r"U:\Python courses PRN\chroma_data.xlsx")
print (data)


# In[3]:


#Let's check the identity of our data 
print type(data)


# In[4]:


#Hum... This a DataFrame ! For further stuff we should turn this into a Numpy Array
#And let's turn it 90° clockwise, it wil be easier to read 
data = data.values.transpose()
print (data)
print ('data is a',type(data),'!')


# In[6]:


#Great, we have our data, properly formated. Now we need the time vector for the plot. 
time = pandas.read_excel(r"U:\Python courses PRN\chroma_time.xlsx")

#Same as above, we should convert it to an array, transpose it and extract only the first episode
#to align all the data on the same time axis 
time = time.values.transpose()[0]

print(time)


# In[7]:


#Now we can start this tremendous figure, first the stage set, we need our friend pyplot for this
from matplotlib import pyplot as plt 

#We are nuts, so let's go for a 3D plot 
from mpl_toolkits.mplot3d import Axes3D

#Prepare the figure
fig = plt.figure()
ax = fig.gca(projection='3d',azim=-110,elev=20)


# In[8]:


#Prepare the different axis
x = time
y = range(data.shape[0])


# In[10]:


X,Y = numpy.meshgrid(x,y)
Z = data


# In[11]:


#Do the surface plot
surface = ax.plot_surface(X,Y,Z,cmap='jet_r')

#Add a few elements
plt.xlabel('Time (s)')
plt.ylabel('Stim #')
           
#And a colorbar
cbar = plt.colorbar(surface,orientation='horizontal')
cbar.ax.set_xlabel('I (pA)')


# In[ ]:


#The plot is not displayed cause JuPyter can't hold 3D views, it should work in ur console ! 

