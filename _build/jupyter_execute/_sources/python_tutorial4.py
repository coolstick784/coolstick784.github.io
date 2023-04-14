#!/usr/bin/env python
# coding: utf-8

# ## Inputting Data

# To input data with a prompt into a variable, we can type
# 
# \<output variable> = input(\<prompt>)

# In[1]:


major = input("What is your major? ")


# In[27]:


print("Your major is", major)


# In[28]:


name = input("What is your name? ")


# Another way to connect strings is to write the + symbol. However, unlike the commas, we'll want to make sure that each specific item is of the _string_ data type

# In[29]:


print(name + " is majoring in " + major)


# In[30]:


print(5 + " is a number")


# In[31]:


print(str(5) + " is a number")

