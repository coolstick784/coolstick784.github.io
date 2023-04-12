#!/usr/bin/env python
# coding: utf-8

# ## Quick Introduction to Pandas

# In Python, there are items called functions. These enable us to format and change the values we're working with. For example, when we print something, we are calling the print() function. By installing code that is compiled into "packages", we can utilize functions that others have created for our own use in a few lines of code.

# One such package is called "pandas". This package lets us work with spreadsheets and create our own in Python. To install a package, simply type "!pip install \<package>" in a cell

# In[1]:


get_ipython().system('pip install pandas')


# Now that we have the functions from the _pandas_ package installed, we can tell Python that we want to import the functions by saying "import pandas". To use a pandas function, we can type "pandas.\<function>". To shorten pandas to pd, we can say "import pandas as pd"

# In[2]:


import pandas as pd


# One data type in Python is called a list, which is made up of a collection of data types. We'll come back to this later, but for now, we can initialize a list of names and values as shown below.

# In[3]:


names = ['Daucus', 'Pastinaca', 'Curucma', 'Nelumbo', 'Artemisia', 'Zingiber']
vals = [34, 18, 16, 20, 29, 19]


# In[4]:


print(names)
print(vals)


# Next, we have a DataFrame. This is similar to an Excel sheet, where we have multiple columns and cells within each column. We can create a data frame out of multiple lists, using the format
# \<dataframe name> = pd.DataFrame(list(zip(\<names of lists separated by commas>))

# In[5]:


df = pd.DataFrame(list(zip(names, vals)))


# In[6]:


df


# Awesome! Now, we want to name the columns. To do this, we can type 
# 
# \<dataframe name>.columns = \[\<list of columns separated by commas]

# In[7]:


df.columns = ['names', 'vals']


# In[8]:


df

