#!/usr/bin/env python
# coding: utf-8

# ## Exercise 4
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

# In[1]:


def HelloWorld():
    print("Hello World!")


# In[2]:


HelloWorld()


# Let's say we want the factorials returned when we call the combination function. Although Python only allows one value to be returned from a function, we can bypass that by combining all the elements into a list

# In[3]:


def combination(n, r):
    n_factorial = factorial(n)
    r_factorial = factorial(r)
    n_r_factorial = factorial(n-r)
    return [n_factorial,r_factorial,(n_factorial/(r_factorial * n_r_factorial))]


# In[4]:


combination(14, 3)

