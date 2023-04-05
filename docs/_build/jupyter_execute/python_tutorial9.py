#!/usr/bin/env python
# coding: utf-8

# ## If Statements

# First, let's ask the user if they use derivatives/integrals in their homework. Then, if they do, we can link them to some helpful resources. If not, we don't need to.

# In[1]:


calc_yn = input("Do you use derivatives/integrals in your homework? Enter Y/N ")


# An 'if' statement essentially means that if a condition is true, we want to do something, and if it doesn't, we want to do something slse. The format goes like:
# 
#   
#     
#     if <condition>:
#         do something
#     else:
#         do something else
#   
#     
# Indentation is really important here, and you'll get an error if you don't include it. The conditions will evaluate to true or false.
# 
# In the code block below, we check if calc_yn is equal to Y (calc_yn == 'Y'). This will give us a True or False answer, which the if statement can then interpret

# In[85]:


if calc_yn == 'Y':
    print("Check out derivative-calculator.com and integral-calculator.com for some help!")
else:
    print("Nice! You're one of the lucky ones")


# Furthermore, if there's more than one scenario, we can use an elif command as well. For example, let's say that if the user enters an invalid response that isn't Y or N, we want to print that there is an error. To do this, we can enter the following code:

# In[86]:


if calc_yn == 'Y':
    print("Check out derivative-calculator.com and integral-calculator.com for some help!")
elif calc_yn == 'N':
    print("Nice! You're one of the lucky ones")
else:
    print("Invalid response")


# An elif statement is placed after an if statement. There do not need to be any elif/else statements, so you can have as many or as little elif statements as you want. However, there can only be one else statement. The format of an if statement goes like this:
# 
#     if <condition>:
#         do something
#     elif <condition 2>: (optional)
#         do something else
#     elif <condition 3>: (optional)
#         do something else
#     ....
#     else: (optional)
#         do something else
