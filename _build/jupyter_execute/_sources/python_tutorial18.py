#!/usr/bin/env python
# coding: utf-8

# ## Dates

# To use dates, we can import the date module from the datetime package. 
# 
# First, we can define a function called printDate(). It will begin by printing the date today, which is shown by date.today().
# 
# To format the date, we can use the .strftime() function, as shown, to format it however you would like

# In[1]:


from datetime import date
# from https://www.programiz.com/python-programming/datetime/current-datetime
def printDate():
    today = date.today()
    print("Hello! The date is: \n", today)
    
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    print("dd/mm/yyyy =", d1)

    # Textual month, day and year	
    d2 = today.strftime("%B %d, %Y")
    print("Month Day, Year =", d2)

    # mm/dd/y
    d3 = today.strftime("%m/%d/%y")
    print("mm/dd/yy =", d3)

    # Month abbreviation, day and year	
    d4 = today.strftime("%b-%d-%Y")
    print("Month-dd-yyyy =", d4)
    return today


# In[2]:


date = printDate()


# In[3]:


print(date)


# Note that when we call printDate(), not only are the printed items in the function printed, but the returned value is shown after the "Out" text.

# In[4]:


printDate()

