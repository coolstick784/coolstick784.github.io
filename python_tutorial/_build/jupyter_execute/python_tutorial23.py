#!/usr/bin/env python
# coding: utf-8

# ## Files and Directories 

# To access and edit directories, we'll want to import the pre-installed os module

# In[1]:


import os


# To get a list of files in your current directory, we can type the listdir() command

# In[2]:


os.listdir()


# To obtain the file path of our current working directory, we can call the getcwd() command

# In[3]:


os.getcwd()


# To change our directory, we can enter the path of the new directory. It can either be relative to the directory at hand or to the computer as a whole

# In[4]:


os.chdir("/Users/schugani")


# In[5]:



os.chdir('Documents')
os.chdir('/Users/schugani')


# To create a folder, we can call the mkdir() function. This path should be relative to the computer.

# First, we can obtain our current directory path

# In[6]:


cur_path = os.getcwd()


# Next, we can name our new folder

# In[7]:


folder_name = "datasets"


# Finally, we can join the two with os.path.join and make a directory based on that

# Here, we can write a try except block that states that if the directory already exists, it will print so and the directory will not be created

# In[8]:


new_dir = os.path.join(cur_path, folder_name)
try:
    os.mkdir(new_dir)
except FileExistsError:
    print("file already exists")


# Let's say we have a file called data.csv and want to move it to our new directory. First, we want to move it to our current directory without Python. Next, we can use os.rename to change the path

# In[9]:


old_path = os.path.join(cur_path, "data.csv")
new_path = os.path.join(new_dir, "data.csv")
os.rename(old_path, new_path)


# In[10]:


os.chdir(new_dir)


# In[11]:


os.listdir()


# Nice! Now our data is in our new directory

# To change our directory back to the old one, we can call the chdir() function with the old path (that we saved as cur_path)

# In[12]:


os.chdir(cur_path)

