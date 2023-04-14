#!/usr/bin/env python
# coding: utf-8

# ## Classes

# Classes in Python can be used to create our own data types with their own functions

# Let's start by creating a class called Dog. With it, we can call the PrintDog function, which prints their name, age, and bark, as well as the isPuppy function, which prints whether or not the dog is a puppy. To initialize the class, we'll want to eneter in the dog's name, age, and bark. By setting bark = "Woof", if bark is not entered, the bark will, by default, be set to "Woof"

# In a class, we'll start with the \_\_init__ function, which initializes the variables in the class. We start with the self argument, which can be accessed by the rest of the class. The self argument is used to access the rest of the variables in the class. For example, self.name will represent the name. Next, we pass in the rest of the parameters -- name, age, and bark. We set the self values so that they can be accessed in other functions.
# 
# Next, we write the other functions, PrintDog and isPuppy

# In[1]:


class Dog:
    def __init__(self, name, age, bark = "Woof"):
        self.name = name
        self.age = age
        self.bark = bark
    def printDog(self):
        print(f"The dog's name is {self.name}, they are {self.age} years old, and they go {self.bark}")
    def isPuppy(self):
        if self.age < 3:
            print(f"{self.name} is a puppy")
        else:
            print(f"{self.name} is not a puppy")


# Let's initialize Fido with a name and age

# In[2]:


fido = Dog("Fido", 5)


# Notice how the default bark is Woof

# In[3]:


fido.printDog()


# We can also set a custom bark with Jack

# In[4]:


jack = Dog("Jack", 2, "arf")


# In[5]:


jack.printDog()


# ### Inheritance
# We can also create new classes based off the "parent" class, which can access the parent class's functions as well as new ones that are defined.
# 
# In this example, we are creating Labradoodle to be a child of the Dog class, which is shown by the Dog being in parenthesis. To initialzie the variables that are in both Labradoodle and Dog, we can use the super().__init__ function, and initialize everything else like the Dog class.
# 
# Variables of the data type Labradoodle can access functions in both the Labradoodle and Dog class, while variables of the data type Dog can only access functions in the Dog class.

# In[6]:


class Labradoodle(Dog):
    def __init__(self, name, age, fur, bark = "Woof"):
        super().__init__(name, age, bark)
        self.fur = fur
    def printFur(self):
        print(self.name + "'s fur is", self.fur)


# In[7]:


will = Labradoodle("Will", 2, "yellow", "awooo")


# In[8]:


will.printDog()


# In[9]:


will.printFur()

