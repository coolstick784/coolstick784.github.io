#!/usr/bin/env python
# coding: utf-8

# ## Numbers

# If we want to round a number, we can use the round() function. Note that this rounds up for .5 and to the nearest number for everything else

# In[1]:


print(round(2.5))
print(round(2.51))


# The abs() command can be used for absolute values

# In[2]:


print(abs(-1))


# Next, we can import the math package. This comes with Python, so you don't need to download anything

# In[3]:


import math


# This allows us to use functions such as math.floor() and math.ceil(), which enable us to round down/up respectively

# In[4]:


print(math.floor(2.9999999999))


# In[5]:


print(math.ceil(2.000000001))

