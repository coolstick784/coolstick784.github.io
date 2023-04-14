#!/usr/bin/env python
# coding: utf-8

# ## Try and Except Statements

# Try and except statements can be used when you encounter an error, but want to do something with it instead of having Python deal with it.

# First, lets define a function called simpleMath which does some simple math

# In[1]:


def simpleMath(x, y):
    
    print("Multiplication: ", x*y)
    print("Addition: ", x + y)
    print("Subtraction: ", x-y)
    print("Division: ", x/y)


# In[2]:


simpleMath(4, 2)


# Note that if we put a string in place instead of a number, an error is given, as we cannot apply mathematical operations to strings

# In[3]:


simpleMath("pizza", 2)


# Let's say that instead of stopping the code with an error, we want to keep running until correct prompts are given. To do this, we can create a while loop with a flag called 'invalid'. Then, we can set up a try except block.
# 
# Try except blocks follow the format:
# 
#     try:
#         <something>
#     except:
#         <something else>
#         
# If an error is given while running something in the try block, the code will immediately go to the except statement. 
# 
# If no error is given and we reach the end of the try block, we can set invalid to false, stopping the loop. Otherwise, a custom error message is given

# In[131]:


invalid = True
while invalid == True:

    try:
        x = float(input("Enter a number: "))
        y = float(input("Enter a second number: "))
        simpleMath(x, y)
        invalid = False
    except:
        print("Invalid inputs. Try again")


# Now, let's say we want to specify by error type. For example, if "pizza" is entered, there is an error because it is a string. If 0 is entered for the second number, there is an error when we divide by 0, as shown:

# In[133]:


x = float(input("Enter a number: "))
y = float(input("Enter a second number: "))
simpleMath(x, y)


# To separate these, we can put an except statement for each error we want to handle, of the format:
# 
#     except <error type>:
#     
# For strings, a ValueError will pop up, and for 0, a ZeroDivisionError will pop up
# 
# We can also put an extra except at the bottom if we wish to handle any other unforseen error.

# In[134]:


invalid = True
while invalid == True:

    try:
        x = float(input("Enter a number: "))
        y = float(input("Enter a second number: "))
        simpleMath(x, y)
        invalid = False
    except ValueError:
        print("Invalid inputs. Try again")
    except ZeroDivisionError:
        print("Zero is in the denominator! Try again")
    except:
        print("There is another error.")

