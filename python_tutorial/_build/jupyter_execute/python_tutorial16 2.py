#!/usr/bin/env python
# coding: utf-8

# ## Dictionaries

# Dictionaries in Python can be used to match certain values up. For example, if we had a list of employees with their names, emails, and phone numbers, we could use a dictionary for each employee to match up their name with a name variable, their email with an email variable, etc.

# We can define a dictionary as follows:
# 
#     <dictionary name> = {<variable name 1>:<variable 1 value>,....<variable name n>:<variable n value>}

# In[1]:


dict1 = {'Name':'John', 'Email':'johnsmith@gmail.com', 'Number':'918-029-0293'}


# In[2]:


dict1


# To reassign a value in the dictionary or to add a new value, simply type
#     
#     <dictionary name>[<name of key>] = <new value>

# In[3]:


dict1['Name'] = 'Mitch'


# In[4]:


dict1['Birthday'] = 'Jan 1 9182'


# In[5]:


dict1


# To view emojis in Python, we can install and load the emoji python

# In[6]:


get_ipython().system('pip install emoji')


# In[7]:


import emoji


# To print an emoji, we can type "emoji.emojize(\<text with emojis>, language = "alias")

# In[8]:


print(emoji.emojize(':smile:', language="alias"))
print(emoji.emojize("Python is :thumbsup:", language="alias"))


# To get the keys (the items corresponding to the definitions, but not the definitions themselves), we can use the keys() function

# In[9]:


dict1.keys()

