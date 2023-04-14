#!/usr/bin/env python
# coding: utf-8

# ## Hangman Exercise (Exercise 7)

# Remember how random.random() generates a number between 0 and 1. Similarly, if you wanted it to generate a number between 1 and 10, we could multiply that by 10. To make sure it goes up to 10 and is not less than 1, we use math.ceil() to round up, as shown:

# In[1]:


import math
import random


# In[2]:


math.ceil(random.random() * 10)


# Here is a quick little code block that applies this to a guessing game. We generate a number, and the user tries to guess it. If the flag (guessed) is not True, we keep going until the user guesses correctly.

# In[3]:


guessed = False
num = math.ceil(random.random() * 10)
while guessed == False:
    guess = int(input("Take a guess: "))
    if guess == num:
        guessed = True
        print("Nice guess!")
    else:
        print("Guess again!")
    


# To generate a list of values in a range, we can use the following code:

# In[146]:


nums = [i for i in range(1, 11)]


# In[147]:


nums


# What this does is it gets each value from the range of 1,11 and adds that to the list, which is nums in this case

# Create a hangman game with these words, but a little simpler. Generate underscores for each letter in the word,
# and print the amount of letters in the word.
#  If a player guesses a letter, each occurence of that letter will be revealed. The player will have 8 lives,
#  and after each guess, the number of lives will be printed out.
#  The game should not be case sensitive
#  
#  Hints:
# 1. Make your word that you print out a list of underscores, and when a player guesses a letter, replace the 
#  corresponding index in the actual word with the underscore in the printed out word. 
# To print out the word with various underscores, write '"".join(word)'
# 2. To get the list of letters in the word, try list(set(selected_word))
# 
# 

# In[148]:


words = ["Apple", "Pear", "Watermelon", "Strawberry", "Banana", "Corn", "Broccoli"]


# ```{admonition} Click to show solution
# :class: dropdown
# 
# 
# 
#     selected = random.choice(words)
#     selected = selected.lower()
#     lives = 8
#     revealed = False
#     word = ["_" for i in range(len(selected))]
#     letters = list(set(selected))
#     while lives > 0 and revealed == False:
#         print(f"Here is the word: There are {len(selected)} letters. \n" )
#         print("".join(word))
# 
# 
#         guess = input("Guess a letter: ").lower()
#         if guess in letters:
#             letters.remove(guess)
#             for idx, letter in enumerate(selected):
#                 if guess == letter:
#                     word[idx] = guess
#         else:
#             print("Wrong guess")
#             lives -= 1
# 
#         if "_" not in word:
#             print("Congratulations! You have won")
#             print("Here is the word: ", selected)
#             revealed = True
#         else:
#             print(f"You have {lives} lives left")
#         if lives == 0:
#             print("You lost")
#         
# ```
