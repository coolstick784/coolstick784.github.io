#!/usr/bin/env python
# coding: utf-8

# ## More Pandas 

# Let's create a data set with some names, ages, and heights

# In[1]:


import pandas as pd


# In[2]:


names = ['John', 'Jeff', 'George']
ages = [12, 20, 34]
heights_ft = ["6'4", "5'7", "5'2"]

df = pd.DataFrame(list(zip(names, ages, heights_ft)))


# In[3]:


df.columns = ['Name', 'Age', 'Height (ft)']


# In[4]:


df


# First, we can convert the height column to two new columns -- feet and inches. This allows us to have the height as a combination of numbers instead of a string, enabling us to perform mathemetical operations on it

# In[5]:


df['Feet'] = [float(i[0]) for i in df['Height (ft)']]
df['In'] = [float(i[2:]) for i in df['Height (ft)']]


# Breaking down the code here, we have 
#      ```df['Feet'] = [float(i[0]) for i in df['Height (ft)']]```
# This says that we want to take float(i\[0]). This is the first element in i. Next, we have "for i in df\\['Height (ft)'\]", which means that each i represents a value in the Height (ft) column. Therefore, for each height, we are taking the first element. Since the height column is a string, this is the first character.
# 
# For inches, we do the same thing, except we take the third character and beyond (i\[2:]). We do this because the first character is the feet, the second character is a ', and everything beyond that is inches.
#     

# To create a new column for the height in centimeters, we can multiply the feet by 12 (because there are 12 inches in a foot) and then by 2.54 (because there are 2.54 cm per inch) and add that to the inches multiplied by 2.54. Something that's really cool about Pandas is that we can add columns like this without any loops or extra code.

# In[6]:


df['Height (cm)'] = df['Feet'] * 12 * 2.54 + df['In'] * 2.54


# In[7]:


df


# To subset data, we first need a list of True/False values that is equal to the length of the data set.

# In[8]:


df['Height (cm)'] > 170


# Then, we can just put that list inside the data frame!

# In[9]:


df[df['Height (cm)'] > 170]


# ### Exercise 8
# Find a subset of df for all people who have more than 3 inches in the 'In' part of their height! Save this to a dataframe called "edited_in"

# ```{admonition} Click to show solution
# :class: dropdown
# 
#         edited_in= df[df['In'] > 3]
# ```

# Similarly, we can do something for people who have less than 5 inches, like this:

# In[10]:


edited_in= df[df['In'] < 5]


# In[11]:


edited_in


# Note how for our edited_in data frame, the row indices go from 0 to 2. To reset this, we can call the reset_index() function

# In[12]:


edited_in.reset_index()


# Awesome! If we don't want our indices saved as a column, we can call the drop=True command from the reset_index function, like so:

# In[13]:


edited_in.reset_index(drop=True)


# However, note that this doesn't save the data frame

# In[14]:


edited_in


# To save the data frame with the resetted indices, we can call the inplace=True command

# In[15]:


edited_in.reset_index(drop=True, inplace=True)


# Alternatively, we could just set it equal to the data frame with the resetted indices

# In[16]:


edited_in = edited_in.reset_index(drop=True)


# In[17]:


edited_in 


# If we wanted to subset by more than one condition, we could incorporate the "&" (and) or "|" (or) symbols, putting each condition in parenthesis. To find all people with an age less than 20 and height more than 170 cm, we could write the following code:

# In[18]:


df[(df['Age'] < 20) & (df['Height (cm)'] > 170)]

