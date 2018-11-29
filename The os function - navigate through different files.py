#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ok let's do this : a script to get data from several files, do an average and then plot the result 
#You should download the "Fake Files" folder. It contains 3 excel files, it contains several measurements
#In 4 conditions A, B, C and D 

#First we import what we'll need 
import os, pandas, numpy
from matplotlib import pyplot as plt


# In[2]:


#Ok now specify the path to the folder containing the files (DON'T FORGET TO CHANGE IT ACCORDING TO YOUR SITUATION !)
path = r"U:\Python courses PRN\Fake Files"


# In[3]:


#Now let's generate a list containing the file names, automatically 
files = os.listdir(path)
print (files)


# In[4]:


#Great, we have the names of the 3 files ! However they are in a weird order... That's something we have to fix. 
#Let's sort them by the alphabetico-numeric order using the sorted() function 
files = sorted(files)
print (files)


# In[5]:


#Much better. Usually this is how files are sorted in Windows/Mac operating systems. 
#Now, the real stuff, we will call the file using a for loop, to operate the average on each file, but first we need to
#Create a container to store the different averages
averages = [] #An empty list (for now !)


# In[6]:


#Now the for loop to compute each file 
for name in files:
    
    #Use pandas to open the excel file 
    data = pandas.read_excel(r"%s\%s"%(path,name))
    print ("Here is the data in %s"%name)
    print data
    
    #Now numpy to perform averaging on DataFrame.values (dataframe to array)
    average = numpy.mean(data.values, axis=0) #The axis refers to direction : 0 for row wise, 1 for column wise
    print ("Here is the average")
    print (average)
    
    #And do not forget to save this average array in the container previously defined 
    averages.append(average)
    
    


# In[7]:


#Ok, you just opened 3 files, did some math on it, in like 5 lines. Amazing :) 
#Now let's go for the plot, that should be a piece of cake so to increase the skill we'll use a loop as well 

#Call the figure
plt.figure()

#We have 3 files, let's say 3 conditions then, let's go for 3 colors 
colors = ['Green','Orange','Blue']

#And now this fancy plot loop 
for i in range(len(averages)):
    plt.plot(averages[i],label=files[i],color=colors[i])
    
#Let's add the legend 
plt.legend(loc='best')

#Show me that plot !! (not required for last Python version)
plt.show()


# In[ ]:




