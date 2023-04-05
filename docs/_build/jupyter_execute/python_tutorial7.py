#!/usr/bin/env python
# coding: utf-8

# ## Strings

# In[1]:


names = ['Daucus', 'Pastinaca', 'Curucma', 'Nelumbo', 'Artemisia', 'Zingiber']


# In[2]:


names


# Strings can also be subset. For example, if we want to find the first character of the first item in the names array, we can type this:

# In[3]:


names[0][0]


# In[4]:


names[1][2:-5]


# Let's break down this code.
# 
# First, names\[1] specifies that we want the second element (the 1 typed + 1 because Python is 0-indexed) oft eh names array
# 
# Second, we are taking a subset, as shown by the ':' character
# 
# Next, we are starting at the third character, as shown by the 2
# 
# Finally, we are taking all numbers up to (but not including!) the 5th to last character, evidenced by the -5

# Another way to put variables in a string is to use f strings. We can do this by typing 'f' before the quotes, and putting all variables in brackets, as shown:

# In[5]:


print(f'{names[0]} is our first name')


# We can also get the length of strings

# In[6]:


len(names[0])


# If we want to make a string all uppercase or all lowercase, we can use the .upper() and .lower() functions

# In[7]:


print(names[0].upper())
print(names[0].lower())


# If we want to find the first location of a characeter in a string, we can use the find function.

# In[8]:


print(names[0].find('a'))


# If we want to replace characters in a string, we can use the replace command. The format of this is
# \<string>.replace(\<characters to replace>, \<new characters>)

# In[9]:


'Daucus'.replace('us', 'dub')


# We can also use the '+=' operator with strings.

# In[10]:


x = 'pizza'
x += " pie"
print(x)


# One other neat function with strings in Python is the .title() function, which capitalizes words as if they were in a title

# In[11]:


'tutorial in python'.title()


# To separate a string by a specific character, we can use the .split() function. Here, we split by spaces, so we end up with a list of words

# In[12]:


"I like pizza".split(" ")

