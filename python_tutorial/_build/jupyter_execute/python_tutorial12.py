#!/usr/bin/env python
# coding: utf-8

# ## Exercise 3

# Let's make a game! Let's say FSU is playing a football game, and is starting the ball at their opponent's 
# 49 yard line. The user will enter an input to pass or run. For each pass, they gain 10 yards, and for 
# each run, they gain 5 yards. However, there is a 10% chance of a turnover each play. The game either ends 
# with a turnover or when FSU reaches the endzone (the opponent 0).
# If the user enters an invalid response, prompt them to enter another.
# After each iteration, print the current yardline/if the ball has been turned over.
# 
# Hint: If random.random() is less than 0.1, there should be a turnover. If not, there should not be

# ```{admonition} Click to show solution
# :class: dropdown
# 
#         cur_ydline = 49
#         turned_over = False
#         while cur_ydline > 0 and turned_over == False:
#             invalid = True
#             while invalid == True:
#                 choice = input("Pass or run? P for pass and R for run: ").upper()
#                 if choice == 'P' or choice == 'R':
#                     invalid = False
#             if random.random() < 0.1:
#                 print("The ball has been turned over. Game over")
#                 turned_over = True
#             elif choice == 'P':
#                 cur_ydline -= 10
#                 print("The pass went for 10 yards! The ball is now at the ", cur_ydline)
#             elif choice == 'R':
#                 cur_ydline -= 5
#                 print("The run went for 5 yards! The ball is now at the ", cur_ydline)
#             if cur_ydline <= 0:
#                 print("Congrats! You won")
# ```
