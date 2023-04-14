#!/usr/bin/env python
# coding: utf-8

# ## Basics: Printing and Basic Arithmetic

# Let's start with the basics. To print something on the screen, we can type "print(\<text>)". If you want to print plain text, you'll want to put that in quotes, as shown below. 

# In[1]:


print("Hello World!")


# In Python, there are different compilers, which are different applications to run the code. Right now, we're in a type of compiler called a notebook. In a notebook, there are items called cells, which is represented by each block of code. If a value is put at the last part of a cell, that value will be printed out in a notebook, as shown.

# In[2]:


"Hello World"


# Next, we have mathematical operators. There are 7 arithmetic ones in python:
# 1. Addition. This is accomplished with the format \<x+y>
# 2. Subtraction, with \<x-y>
# 3. Multiplication, with \<x*y>
# 4. Division, with \<x/y>
# 5. Exponents, with \<x\**y> representing x^y
# 6. Modulus, which represents a remainder. For example, if we divide 5/2, we will end up with a remainder of 1. This is accomplished with the format \<x%y>
# 7. Floor division, which represents the rounded down number of division, represented by //. For example, 11//2 wil equal 5.
# 

# In[3]:


print(1+1)
print(5-2)
print(3*4)
print(9/2)
print(2**5)
print(9%2)
print(15//7)


# After that, we have variables. To assign variables, we can type 
# 
# \<variable we want to assign> = \<what we want in the variable>.
# 
# For example, if we type "x = 2\*3", we are assigning the value of 2\*3 to the variable x

# In[4]:


x = 2 * 3
y = 5 - 2
g = 9/2
p = 9 % 2


# We can also apply multiplication to strings. For example, we can print "Hello World" 10 times like this:

# In[5]:


print("Hello World" * 10)


# To print multiple values at a time, one way we can do this is we can separate them by commas

# In[6]:


print(x, y, g, p)


# To change a value by an operator, we can use the \<operator>= operators. For example, the variable x is equal to 6 right now. If we want to subtract that by 2, we can type x-=2

# In[7]:


x-=2


# Now, x should print out 4

# In[8]:


x


# Similarly, we can make x equal to x^2 with x**=2

# In[9]:


x**= 2
x


# Next, we have the equality operator. This outputs "True" if the two items are equal and "False" if they are not
# 

# In[10]:


print("Is 7==7?", 7==7)
print("Is x==0?", x==0)

