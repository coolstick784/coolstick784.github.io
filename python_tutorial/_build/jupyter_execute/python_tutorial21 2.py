#!/usr/bin/env python
# coding: utf-8

# ### Inheritance

# We can also create new classes based off the "parent" class, which can access the parent class's functions as well as new ones that are defined.
# 
# In this example, we are creating Labradoodle to be a child of the Dog class, which is shown by the Dog being in parenthesis. To initialzie the variables that are in both Labradoodle and Dog, we can use the super().\_\_init__ function, and initialize everything else like the Dog class.
# 
# Variables of the data type Labradoodle can access functions in both the Labradoodle and Dog class, while variables of the data type Dog can only access functions in the Dog class.

# In[1]:


class Labradoodle(Dog):
    def __init__(self, name, age, fur, bark = "Woof"):
        super().__init__(name, age, bark)
        self.fur = fur
    def printFur(self):
        print(self.name + "'s fur is", self.fur)


# In[141]:


will = Labradoodle("Will", 2, "yellow", "awooo")


# In[142]:


will.printDog()


# In[143]:


will.printFur()

