#!/usr/bin/env python
# coding: utf-8

# ### PROBLEM 2

# In[14]:


### Loading and using cars to dispay cars.iloc to only display Odd Numbers due to slicing.

odd_columns = cars.iloc[:5,::2]
odd_columns


# In[16]:


### The row of Mazda RX4 is accessible due to the variable 'mazda' being used to store the row

mazda = cars[cars['Model'] == 'Mazda RX4']
print("\033[1m Row '0' is the row that contains Mazda RX4':\033[0m\n")
mazda


# In[18]:


### The number of cylinder in the car Camaro z28 is now accessible due to the varibalbe 'camaro'

print("\033[1mHere are the number of cyliders in the car Camaro z28:\033[0m:\n")
camaro = cars[cars['Model'] == 'Camaro Z28']['cyl'].values[0]
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]


# In[20]:


### The variable 'both' was used to store the data containing the cylinders and gears of the given cars

print("\033[1mCylinders and Gears for the following cars: Mazda RX4, Ford Pantera L, and Honda Civic\033[0m:\n")
both = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
selected_cars = cars[cars['Model'].isin(both)][['Model', 'cyl', 'gear']]
selected_cars


# In[ ]:




