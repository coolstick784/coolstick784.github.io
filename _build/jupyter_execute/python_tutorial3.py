#!/usr/bin/env python
# coding: utf-8

# ## Data Types

# The four major basic data types in Python are integers, decimals/floats, booleans, and strings. Integers are whole numbers, floats are decimals, booleans are true/false values, and strings are a sequence of characters 

# To start, let's set the value of "val" to 1 in quotation marks, which indicates that it's a string

# In[1]:


val = "1"
type(val)


# To convert a value to a different data type, we can type \<data type>(\<variable name>)
# 
# We can see how the value "1" is converted to other data types. All values that are not equal to 0/a blank string will equal true in boolean

# In[2]:


print("integer", int(val))
print("float/decimal", float(val))
print("boolean", bool(val))
print("string", val)


# In[3]:


print("Boolean of -0.00001:", bool(-0.00001))
print("Boolean of 0:", bool(0))
print("Boolean of an empty string:", bool(""))

