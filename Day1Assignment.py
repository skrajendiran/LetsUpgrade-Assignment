#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as pl


# In[42]:


#Assignment 1 

x= np.arange(0,11)
y= x*x
pl.plot(x,y,color='green', marker='o', linestyle='dashed',linewidth=2, markersize=10)
pl.title("LinePlot")
pl.xlabel("xaxis")
pl.ylabel("yaxis")


# In[43]:


# Assignment 2 :Plotting Days against sales

a=[1,2,3,4,5,6,7]
b=[160,150,140,145,175,165,180]
pl.plot(a,b)
pl.title("Day Sales")
pl.xlabel("Day")
pl.ylabel("Sales")






