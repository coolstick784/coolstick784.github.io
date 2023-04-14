#!/usr/bin/env python
# coding: utf-8

# ## Exercise 8
# Find a subset of df for all people who have more than 3 inches in the 'In' part of their height! Save this to a dataframe called "edited_in"

# ```{admonition} Click to show solution
# :class: dropdown
# 
#         edited_in= df[df['In'] > 3]
# ```

# Similarly, we can do something for people who have less than 5 inches, like this:

# In[1]:


edited_in= df[df['In'] < 5]


# In[178]:


edited_in


# Note how for our edited_in data frame, the row indices go from 0 to 2. To reset this, we can call the reset_index() function

# In[179]:


edited_in.reset_index()


# Awesome! If we don't want our indices saved as a column, we can call the drop=True command from the reset_index function, like so:

# In[180]:


edited_in.reset_index(drop=True)


# However, note that this doesn't save the data frame

# In[181]:


edited_in


# To save the data frame with the resetted indices, we can call the inplace=True command

# In[182]:


edited_in.reset_index(drop=True, inplace=True)


# Alternatively, we could just set it equal to the data frame with the resetted indices

# In[183]:


edited_in = edited_in.reset_index(drop=True)


# In[184]:


edited_in 


# If we wanted to subset by more than one condition, we could incorporate the "&" (and) or "|" (or) symbols, putting each condition in parenthesis. To find all people with an age less than 20 and height more than 170 cm, we could write the following code:

# In[185]:


df[(df['Age'] < 20) & (df['Height (cm)'] > 170)]

