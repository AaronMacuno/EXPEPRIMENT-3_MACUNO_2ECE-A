#!/usr/bin/env python
# coding: utf-8

# ### PROBLEM 1

# In[2]:


### Importing numpy
import numpy as np

### Importing pandas
import pandas as pd

### Loading the 'cars.csv' file and storing it inside the variable "cars"
cars = pd.read_csv('cars.csv')

### Printing the variable "cars"
cars


# In[4]:


### This prints the first 5 rows of cars inside 'cars.csv'

cars.head()


# In[6]:


### This prints the last 5 rows of cars inside 'cars.csv'

cars.tail()


# In[ ]:




