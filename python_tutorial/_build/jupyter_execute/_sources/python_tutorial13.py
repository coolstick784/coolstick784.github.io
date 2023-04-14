#!/usr/bin/env python
# coding: utf-8

# ## Arrays, Functions, and Nested Loops

# Another built-in package in Python is the array package.

# In[1]:


from array import *


# In[2]:


arr = [[1,2,3], [4, 5, 6], [7, 8, 9], [10, 11]]


# To access the nth list in the array, we can use arr\[\<index>], and we can access elements in said list just like how we would with regular lists

# In[3]:


arr[0] # the first list


# In[4]:


arr[0][2] # the third element in the first list


# In[5]:



for a in arr:
    for b in a:
        print(b, end = " ")
    


# Let's say we have the array above. This is a 2D list, or a list of lists, which is called an array. What we're doing here is saying for a in arr (for each list in the list), we want to select each item in the list (for b in a). Then, for each item in each list, we want to print it, ending with a space to separate each element by a space. Afer that, 

# In[6]:


arr = [[1,2,3], [4, 5, 6], [7, 8, 9], [10, 11]]
for a in arr:
    for b in a:
        print(b, end = " ")
    
    print("\n")


# After that, we can separate the items in each list with a "\n" (new line character) between each list. This can be done after we're iterating through each list, which is inside the first loop but not the second. Play around with it if you're a bit confused -- that might help you understand it a little more!

# Now, we csn start to write our own functions. Functions take 0 to infinite inputs, and can return up to 1 item in Python. They are in the format
# 
#     def <function name>(<inputs>):
#         content of function
#         return <outputs>
#         
# Functions can also reference other functions

# Let's try to make a function returning a combination given two numbers, n and r. First, combinations are built on factorials, so let's make a factorial function. 

# In[7]:


def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output


# Taking in an input n, we start by setting the output to 1. Then, for each number from 1 to n (including n), we multiply the output by that. Finally, we return the ending output.

# In[8]:


def combination(n, r):
    n_factorial = factorial(n)
    r_factorial = factorial(r)
    n_r_factorial = factorial(n-r)
    return (n_factorial/(r_factorial * n_r_factorial))


# To get the combination of n and r, we get the factorials of n and r, then the factorial of n-r, and finally calculate the combinations, returning the end result

# To call a function, we type \<function name>(\<function inputs>)

# In[9]:


combination(14, 3)


# ### Exercise 4
# 
# Try to make a function called permutation that takes two numbers, n and r, and returns
# 
# n!/(n-r)! (! is the factorial symbol)

# ```{admonition} Click to show solution
# :class: dropdown
#         def permutation(n, r):
#             n_factorial = factorial(n)
#             n_r_factorial = factorial(n-r)
#             return (n_factorial/(n_r_factorial))
# ```

# Here is a function with no inputs, but still does something. This is useful if, for example, you want to print a lot of text every time something happens.

# In[10]:


def HelloWorld():
    print("Hello World!")


# In[11]:


HelloWorld()


# Let's say we want the factorials returned when we call the combination function. Although Python only allows one value to be returned from a function, we can bypass that by combining all the elements into a list

# In[12]:


def combination(n, r):
    n_factorial = factorial(n)
    r_factorial = factorial(r)
    n_r_factorial = factorial(n-r)
    return [n_factorial,r_factorial,(n_factorial/(r_factorial * n_r_factorial))]


# In[13]:


combination(14, 3)


# In[ ]:




