#!/usr/bin/env python
# coding: utf-8

# ## Exercise 2

# Ask the user if they are an undergraduate or graduate student. If they are a grad student, link them to https://gradschool.fsu.edu/ . Otherwise, link them to fsu.edu . If neither are entered, print that there is an invalid response. Responses should NOT be case sensitive
# 
# Hint: Convert the input to lowercase after reading it in, and make everything else you're comparing it to is lowercase as well

# ```{admonition} Click to show solution
# :class: dropdown
#         grad_undergrad = input("Are you a grad (G) or undergrad (U) student").lower()
#         if grad_undergrad == "g":
#             print("Here is your homepage: gradschool.fsu.edu")
#         elif grad_undergrad == "u":
#             print("Here is your homepage: fsu.edu")
#         else:
#             print("Invalid Response")
# ```
