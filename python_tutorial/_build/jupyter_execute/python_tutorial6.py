#!/usr/bin/env python
# coding: utf-8

# ## Lists and Sets

# Going back to our lists of names and values, we'll reinitialize them as shown:

# In[1]:


names = ['Daucus', 'Pastinaca', 'Curucma', 'Nelumbo', 'Artemisia', 'Zingiber']
vals = [34, 18, 16, 20, 29, 19]


# If we make vals a set, this would essentially make it an ordered list that cannot be altered with only unique values

# In[2]:


set(vals)


# In[3]:


set([16, 17, 17, 18, 20, 19, 19, 19, 19, 19])


# To sort a list, we can use the .sort() function

# In[4]:


vals.sort()


# In[5]:


vals


# To get the maximum, minimum, and sum of a list of numbers, we can use the following commands:

# In[6]:


print("max:", max(vals))
print("min", min(vals))
print("sum:", sum(vals))


# To get a description of a list of numbers all at once, we can convert the list to a Series object and then apply the describe command, as shown:

# In[7]:


pd.Series(vals).describe()


# In python, lists are 0-indexed. This means that the index of the 1st element will be 0, so to access the 1st element of a list, we will want to type \<name of list>\[0]. Similarly, for the second item, it will have an index of 1

# In[39]:


vals[1]


# In[40]:


names[0]


# The last element of the list also has an index of -1, the second last element has an index of -2, etc.

# In[41]:


names[-1]


# In[42]:


numbers = [20, 5, 4, 6, 2]


# To add an item to a list, we can use the .append() commamd

# In[43]:


numbers.append(44)
numbers


# To insert a value into a specific index, we can use the .insert() command, which takes two arguments. The first one is the index to put the value and the second is the value itself

# In[44]:


numbers.insert(2, 100)


# In[45]:


numbers


# To find the index of a value, we can use the .index() function

# In[46]:


numbers.index(20)


# To remove a value based on the value and not the index of the value, we can use the .remove() command. Note that this only removes the first instance of the value and not all of them

# In[47]:


numbers.append(4)
numbers.append(4)
numbers


# In[48]:


numbers.remove(4)
numbers


# In[49]:


numbers


# To remove a value based on the index, we can use the "del" function

# In[50]:


del numbers[2]


# In[51]:


numbers


# To remove the value based on the index and print the removed number, we can use the pop command

# In[52]:


numbers.pop(3)


# In[53]:


numbers


# To obtsin a subset of values based on their indexes, we can use the following command:
#     
# \<list of values>\[\<start of subset>:\<end of subset>]

# In[54]:


numbers[0:3]


# If we want to copy a list, make sure to use the .copy() command. Here, we can see what happens if we copy numbers to numbers3

# In[55]:


numbers3 = numbers


# In[56]:


numbers3


# Notice that if we add 5 to the end of numbers3, it also gets added to numbers!

# In[57]:


numbers3.append(5)


# In[58]:


print(numbers3)
print(numbers)


# As you can see, although we only changed numbers3, numbers got changed as well

# In[59]:


numbers4=numbers.copy()
numbers4.append(6)
print(numbers4)
print(numbers)


# To get the unique values of a list in a new, ordered, list, we can take a list of the set of the list

# In[60]:


numbers = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 5, 5, 4, 3, 6, 5, 2, 0 , 1, 44]


# In[61]:


list(set(numbers))


# To get the length of a list, we can use the len() function

# In[62]:


numbers


# In[63]:


len(numbers)


# To join elements in a list, we can use the join() function

# In[64]:


apple = ['A', 'p', 'p', 'l', 'e']
print("With no spaces:", "".join(apple))
print("With a space in between:", " ".join(apple))

