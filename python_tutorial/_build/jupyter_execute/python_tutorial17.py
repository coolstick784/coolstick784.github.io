#!/usr/bin/env python
# coding: utf-8

# ## Exercise 6
# Ask the user for an input. If any of the words in this list are detected, replace them with emojis.
# 
# 
# 
# 
# Hint: Split the input for each word and check if the word is in the list from there

# In[1]:


emoji_dict = {':)':':slightly_smiling_face:', ':D':':smile:', ':/':':confused:', ';)':':wink:', ':O':':open_mouth:'}


# ```{admonition} Click to show solution
# :class: dropdown
# 
#         
#         words = input("say something")
#         new_words = words
#         for word in words.split(" "):
# 
#             if word in list(emoji_dict.keys()):
# 
#                 new_words=new_words.replace(word, emoji_dict[word])
#         print(emoji.emojize(new_words, language="alias"))
# ```
