#!/usr/bin/env python
# coding: utf-8

# ## Loops

# In[1]:


names = ['Daucus', 'Pastinaca', 'Curucma', 'Nelumbo', 'Artemisia', 'Zingiber']


# Let's say we want to make a list containing True/False values for if P is in each name.

# To iterate through a list, we can use the following code:
#     
#     for <item name of your choice> in <list>:

# In[2]:


for name in names:
    print(name)


# Next, we can initialize a list to save our values in

# In[3]:


p_list = []


# What we're doing here is saying that for each name, we're appending an item to p_list. That item is equal to the value "'P' in name", which is True if P is in the name and False if not

# In[4]:


for name in names:
    p_list.append('P' in name)


# In[5]:


p_list


# Another way to do this is through list comprehension.
# 
# Breaking down the code below, we're asking Python if 'P' is in the name. If it is, we'll get True, and if not, we'll get False. Then, we do this for each name in names, which should gives us the same values as p_list

# In[6]:


print(['P' in name for name in names])


# Similarly, we can save the value as 'name' (meaning the name itself) for each name in names. At the end, there's a caveat; this only applies if the length of the name is greater than 7. Thus, this returns each name with a length of 8 or more.

# In[7]:


[name for name in names if len(name) > 7]


# Next, we have while loops. This is of the format
# 
#     
#     while <condition>:
#         do something
# 
# Let's say that we want to print "i like pizza" 10 times. To do this, we can start by initializing a variable, i, at 0. We can add 1 to i for each iteration, and after 10 iterations, i will then be equal to 10. Then, we can set the condition to "i<10" because then after 10 iterations, the condiiton will then be false and the loop will stop.

# In[8]:


i= 0
while i < 10:
    print("i like pizza")
    i += 1


# To do something in a for loop n times, we can say
#     
#     for <variable name of your choice> in range(n):
#         do something

# In[9]:


for i in range(10):
    print("i like pizza")


# One use for while loops is a flag. For example, if you're making a game, you might want a variable called GameRunning to tell the computer if the game is still running or not. If it's not running, you'll stop the code. Another use of this is to not stop when given an invalid response, and to keep prompting the user until they've entered something of your liking.
# 
# 

# In[10]:


flag = False
while flag == False:
    name = input("Enter the name 'John'")
    if name == 'John':
        flag = True


# What we can see here is that while the flag of 'John' being entered is still false, the user will keep being prompted. Then, when the name is John, the flag will be set to True and the loop will stop.

# Another built-in Python package is random. We can use functions such as random.random(), which generate a random number between 0 and 1, and random.choice(\<list name>), which generates a random item from the list

# In[97]:


import random


# In[98]:


random.random()


# In[99]:


names


# In[100]:


random.choice(names)

