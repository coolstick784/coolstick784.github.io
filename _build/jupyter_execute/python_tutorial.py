#!/usr/bin/env python
# coding: utf-8

# # Tutorial

# Before we start, please make sure you have Python installed from https://www.python.org/

# ## Basics: Printing and Basic Arithmetic

# Let's start with the basics. To print something on the screen, we can type "print(\<text>)". If you want to print plain text, you'll want to put that in quotes, as shown below. 

# In[1]:


print("Hello World!")


# In Python, there are different compilers, which are different applications to run the code. Right now, we're in a type of compiler called a notebook. In a notebook, there are items called cells, which is represented by each block of code. If a value is put at the last part of a cell, that value will be printed out in a notebook, as shown.

# In[2]:


"Hello World"


# Next, we have mathematical operators. There are 7 arithmetic ones in python:
# 1. Addition. This is accomplished with the format \<x+y>
# 2. Subtraction, with \<x-y>
# 3. Multiplication, with \<x*y>
# 4. Division, with \<x/y>
# 5. Exponents, with \<x\**y> representing x^y
# 6. Modulus, which represents a remainder. For example, if we divide 5/2, we will end up with a remainder of 1. This is accomplished with the format \<x%y>
# 7. Floor division, which represents the rounded down number of division, represented by //. For example, 11//2 wil equal 5.
# 

# In[3]:


print(1+1)
print(5-2)
print(3*4)
print(9/2)
print(2**5)
print(9%2)
print(15//7)


# After that, we have variables. To assign variables, we can type 
# 
# \<variable we want to assign> = \<what we want in the variable>.
# 
# For example, if we type "x = 2\*3", we are assigning the value of 2\*3 to the variable x

# In[4]:


x = 2 * 3
y = 5 - 2
g = 9/2
p = 9 % 2


# We can also apply multiplication to strings. For example, we can print "Hello World" 10 times like this:

# In[5]:


print("Hello World" * 10)


# To print multiple values at a time, one way we can do this is we can separate them by commas

# In[6]:


print(x, y, g, p)


# To change a value by an operator, we can use the \<operator>= operators. For example, the variable x is equal to 6 right now. If we want to subtract that by 2, we can type x-=2

# In[7]:


x-=2


# Now, x should print out 4

# In[8]:


x


# Similarly, we can make x equal to x^2 with x**=2

# In[9]:


x**= 2
x


# Next, we have the equality operator. This outputs "True" if the two items are equal and "False" if they are not
# 

# In[10]:


print("Is 7==7?", 7==7)
print("Is x==0?", x==0)


# ## Quick Introduction to Pandas

# In Python, there are items called functions. These enable us to format and change the values we're working with. For example, when we print something, we are calling the print() function. By installing code that is compiled into "packages", we can utilize functions that others have created for our own use in a few lines of code.

# One such package is called "pandas". This package lets us work with spreadsheets and create our own in Python. To install a package, simply type "!pip install \<package>" in a cell

# In[11]:


get_ipython().system('pip install pandas')


# Now that we have the functions from the _pandas_ package installed, we can tell Python that we want to import the functions by saying "import pandas". To use a pandas function, we can type "pandas.\<function>". To shorten pandas to pd, we can say "import pandas as pd"

# In[12]:


import pandas as pd


# One data type in Python is called a list, which is made up of a collection of data types. We'll come back to this later, but for now, we can initialize a list of names and values as shown below.

# In[13]:


names = ['Daucus', 'Pastinaca', 'Curucma', 'Nelumbo', 'Artemisia', 'Zingiber']
vals = [34, 18, 16, 20, 29, 19]


# In[14]:


print(names)
print(vals)


# Next, we have a DataFrame. This is similar to an Excel sheet, where we have multiple columns and cells within each column. We can create a data frame out of multiple lists, using the format
# \<dataframe name> = pd.DataFrame(list(zip(\<names of lists separated by commas>))

# In[15]:


df = pd.DataFrame(list(zip(names, vals)))


# In[16]:


df


# Awesome! Now, we want to name the columns. To do this, we can type 
# 
# \<dataframe name>.columns = \[\<list of columns separated by commas]

# In[17]:


df.columns = ['names', 'vals']


# In[18]:


df


# ## Data Types

# The four major basic data types in Python are integers, decimals/floats, booleans, and strings. Integers are whole numbers, floats are decimals, booleans are true/false values, and strings are a sequence of characters 

# To start, let's set the value of "val" to 1 in quotation marks, which indicates that it's a string

# In[19]:


val = "1"
type(val)


# To convert a value to a different data type, we can type \<data type>(\<variable name>)
# 
# We can see how the value "1" is converted to other data types. All values that are not equal to 0/a blank string will equal true in boolean

# In[20]:


print("integer", int(val))
print("float/decimal", float(val))
print("boolean", bool(val))
print("string", val)


# In[21]:


print("Boolean of -0.00001:", bool(-0.00001))
print("Boolean of 0:", bool(0))
print("Boolean of an empty string:", bool(""))


# ## Inputting Data

# To input data with a prompt into a variable, we can type
# 
# \<output variable> = input(\<prompt>)

# In[22]:


major = input("What is your major? ")


# In[27]:


print("Your major is", major)


# In[28]:


name = input("What is your name? ")


# Another way to connect strings is to write the + symbol. However, unlike the commas, we'll want to make sure that each specific item is of the _string_ data type

# In[29]:


print(name + " is majoring in " + major)


# In[30]:


print(5 + " is a number")


# In[31]:


print(str(5) + " is a number")


# ## Exercise 1
# 
# For an exercise, ask the user for the temperature in Fahrenheit and convert it to Celsius.
# 
# Celsius = (Fahrenheit - 32)\*5/9
# 
# Hint: Convert the input to a float before converting!

# ```{admonition} Click to show solution
# :class: dropdown
#         temp_f = input("What is the temperature in Fahrenheit?")
#         temp_c = (float(temp_f)-32)* 5/9
#         print("The temperature in Celsius is ", temp_c)```
# 

# ## Lists and Sets

# Going back to our lists of names and values, we'll reinitialize them as shown:

# In[32]:


names = ['Daucus', 'Pastinaca', 'Curucma', 'Nelumbo', 'Artemisia', 'Zingiber']
vals = [34, 18, 16, 20, 29, 19]


# If we make vals a set, this would essentially make it an ordered list that cannot be altered with only unique values

# In[33]:


set(vals)


# In[34]:


set([16, 17, 17, 18, 20, 19, 19, 19, 19, 19])


# To sort a list, we can use the .sort() function

# In[35]:


vals.sort()


# In[36]:


vals


# To get the maximum, minimum, and sum of a list of numbers, we can use the following commands:

# In[37]:


print("max:", max(vals))
print("min", min(vals))
print("sum:", sum(vals))


# To get a description of a list of numbers all at once, we can convert the list to a Series object and then apply the describe command, as shown:

# In[38]:


pd.Series(vals).describe()


# In python, lists are 0-indexed. This means that the index of the 1st element will be 0, so to access the 1st element of a list, we will want to type \<name of list>\[0]. Similarly, for the second item, it will have an index of 1

# In[39]:


vals[1]


# In[40]:


names[0]


# The last element of the list also has an index of -1, the second last element has an index of -2, etc.

# In[41]:


names[-1]


# In[42]:


numbers = [20, 5, 4, 6, 2]


# To add an item to a list, we can use the .append() commamd

# In[43]:


numbers.append(44)
numbers


# To insert a value into a specific index, we can use the .insert() command, which takes two arguments. The first one is the index to put the value and the second is the value itself

# In[44]:


numbers.insert(2, 100)


# In[45]:


numbers


# To find the index of a value, we can use the .index() function

# In[46]:


numbers.index(20)


# To remove a value based on the value and not the index of the value, we can use the .remove() command. Note that this only removes the first instance of the value and not all of them

# In[47]:


numbers.append(4)
numbers.append(4)
numbers


# In[48]:


numbers.remove(4)
numbers


# In[49]:


numbers


# To remove a value based on the index, we can use the "del" function

# In[50]:


del numbers[2]


# In[51]:


numbers


# To remove the value based on the index and print the removed number, we can use the pop command

# In[52]:


numbers.pop(3)


# In[53]:


numbers


# To obtsin a subset of values based on their indexes, we can use the following command:
#     
# \<list of values>\[\<start of subset>:\<end of subset>]

# In[54]:


numbers[0:3]


# If we want to copy a list, make sure to use the .copy() command. Here, we can see what happens if we copy numbers to numbers3

# In[55]:


numbers3 = numbers


# In[56]:


numbers3


# Notice that if we add 5 to the end of numbers3, it also gets added to numbers!

# In[57]:


numbers3.append(5)


# In[58]:


print(numbers3)
print(numbers)


# As you can see, although we only changed numbers3, numbers got changed as well

# In[59]:


numbers4=numbers.copy()
numbers4.append(6)
print(numbers4)
print(numbers)


# To get the unique values of a list in a new, ordered, list, we can take a list of the set of the list

# In[60]:


numbers = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 5, 5, 4, 3, 6, 5, 2, 0 , 1, 44]


# In[61]:


list(set(numbers))


# To get the length of a list, we can use the len() function

# In[62]:


numbers


# In[63]:


len(numbers)


# To join elements in a list, we can use the join() function

# In[64]:


apple = ['A', 'p', 'p', 'l', 'e']
print("With no spaces:", "".join(apple))
print("With a space in between:", " ".join(apple))


# ## Strings

# In[65]:


names


# Strings can also be subset. For example, if we want to find the first character of the first item in the names array, we can type this:

# In[66]:


names[0][0]


# In[70]:


names[1][2:-5]


# Let's break down this code.
# 
# First, names\[1] specifies that we want the second element (the 1 typed + 1 because Python is 0-indexed) oft eh names array
# 
# Second, we are taking a subset, as shown by the ':' character
# 
# Next, we are starting at the third character, as shown by the 2
# 
# Finally, we are taking all numbers up to (but not including!) the 5th to last character, evidenced by the -5

# Another way to put variables in a string is to use f strings. We can do this by typing 'f' before the quotes, and putting all variables in brackets, as shown:

# In[71]:


print(f'{names[0]} is our first name')


# We can also get the length of strings

# In[72]:


len(names[0])


# If we want to make a string all uppercase or all lowercase, we can use the .upper() and .lower() functions

# In[73]:


print(names[0].upper())
print(names[0].lower())


# If we want to find the first location of a characeter in a string, we can use the find function.

# In[74]:


print(names[0].find('a'))


# If we want to replace characters in a string, we can use the replace command. The format of this is
# \<string>.replace(\<characters to replace>, \<new characters>)

# In[75]:


'Daucus'.replace('us', 'dub')


# We can also use the '+=' operator with strings.

# In[76]:


x = 'pizza'
x += " pie"
print(x)


# One other neat function with strings in Python is the .title() function, which capitalizes words as if they were in a title

# In[77]:


'tutorial in python'.title()


# To separate a string by a specific character, we can use the .split() function. Here, we split by spaces, so we end up with a list of words

# In[78]:


"I like pizza".split(" ")


# ## Numbers

# If we want to round a number, we can use the round() function. Note that this rounds up for .5 and to the nearest number for everything else

# In[79]:


print(round(2.5))
print(round(2.51))


# The abs() command can be used for absolute values

# In[80]:


print(abs(-1))


# Next, we can import the math package. This comes with Python, so you don't need to download anything

# In[81]:


import math


# This allows us to use functions such as math.floor() and math.ceil(), which enable us to round down/up respectively

# In[82]:


print(math.floor(2.9999999999))


# In[83]:


print(math.ceil(2.000000001))


# ## If Statements

# First, let's ask the user if they use derivatives/integrals in their homework. Then, if they do, we can link them to some helpful resources. If not, we don't need to.

# In[84]:


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

# ## Loops

# In[87]:


names = ['Daucus', 'Pastinaca', 'Curucma', 'Nelumbo', 'Artemisia', 'Zingiber']


# Let's say we want to make a list containing True/False values for if P is in each name.

# To iterate through a list, we can use the following code:
#     
#     for <item name of your choice> in <list>:

# In[88]:


for name in names:
    print(name)


# Next, we can initialize a list to save our values in

# In[89]:


p_list = []


# What we're doing here is saying that for each name, we're appending an item to p_list. That item is equal to the value "'P' in name", which is True if P is in the name and False if not

# In[90]:


for name in names:
    p_list.append('P' in name)


# In[91]:


p_list


# Another way to do this is through list comprehension.
# 
# Breaking down the code below, we're asking Python if 'P' is in the name. If it is, we'll get True, and if not, we'll get False. Then, we do this for each name in names, which should gives us the same values as p_list

# In[92]:


print(['P' in name for name in names])


# Similarly, we can save the value as 'name' (meaning the name itself) for each name in names. At the end, there's a caveat; this only applies if the length of the name is greater than 7. Thus, this returns each name with a length of 8 or more.

# In[93]:


[name for name in names if len(name) > 7]


# Next, we have while loops. This is of the format
# 
#     
#     while <condition>:
#         do something
# 
# Let's say that we want to print "i like pizza" 10 times. To do this, we can start by initializing a variable, i, at 0. We can add 1 to i for each iteration, and after 10 iterations, i will then be equal to 10. Then, we can set the condition to "i<10" because then after 10 iterations, the condiiton will then be false and the loop will stop.

# In[94]:


i= 0
while i < 10:
    print("i like pizza")
    i += 1


# To do something in a for loop n times, we can say
#     
#     for <variable name of your choice> in range(n):
#         do something

# In[95]:


for i in range(10):
    print("i like pizza")


# One use for while loops is a flag. For example, if you're making a game, you might want a variable called GameRunning to tell the computer if the game is still running or not. If it's not running, you'll stop the code. Another use of this is to not stop when given an invalid response, and to keep prompting the user until they've entered something of your liking.
# 
# 

# In[96]:


flag = False
while flag == False:
    name = input("Enter the name 'John'")
    if name == 'John':
        flag = True


# What we can see here is that while the flag of 'John' being entered is still false, the user will keep being prompted. Then, when the name is John, the flag will be set to True and the loop will stop.

# Another built-in Python package is random. We can use functions such as random.random(), which generate a random number between 0 and 1, and random.choice(\<list name>), which generates a random item from the list

# In[97]:


import random


# In[98]:


random.random()


# In[99]:


names


# In[100]:


random.choice(names)


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

# ## Arrays, Functions, and Nested Loops

# Another built-in package in Python is the array package.

# In[101]:


from array import *


# In[102]:


arr = [[1,2,3], [4, 5, 6], [7, 8, 9], [10, 11]]


# To access the nth list in the array, we can use arr\[\<index>], and we can access elements in said list just like how we would with regular lists

# In[103]:


arr[0] # the first list


# In[104]:


arr[0][2] # the third element in the first list


# In[105]:



for a in arr:
    for b in a:
        print(b, end = " ")
    


# Let's say we have the array above. This is a 2D list, or a list of lists, which is called an array. What we're doing here is saying for a in arr (for each list in the list), we want to select each item in the list (for b in a). Then, for each item in each list, we want to print it, ending with a space to separate each element by a space. Afer that, 

# In[106]:


arr = [[1,2,3], [4, 5, 6], [7, 8, 9], [10, 11]]
for a in arr:
    for b in a:
        print(b, end = " ")
    
    print("\n")


# After that, we can separate the items in each list with a "\n" (new line character) between each list. This can be done after we're iterating through each list, which is inside the first loop but not the second. Play around with it if you're a bit confused -- that might help you understand it a little more!

# Now, we csn start to write our own functions. Functions take 0 to infinite inputs, and can return up to 1 item in Python. They are in the format
# 
#     def <function name>(<inputs>):
#         content of function
#         return <outputs>
#         
# Functions can also reference other functions

# Let's try to make a function returning a combination given two numbers, n and r. First, combinations are built on factorials, so let's make a factorial function. 

# In[107]:


def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output


# Taking in an input n, we start by setting the output to 1. Then, for each number from 1 to n (including n), we multiply the output by that. Finally, we return the ending output.

# In[108]:


def combination(n, r):
    n_factorial = factorial(n)
    r_factorial = factorial(r)
    n_r_factorial = factorial(n-r)
    return (n_factorial/(r_factorial * n_r_factorial))


# To get the combination of n and r, we get the factorials of n and r, then the factorial of n-r, and finally calculate the combinations, returning the end result

# To call a function, we type \<function name>(\<function inputs>)

# In[109]:


combination(14, 3)


# ## Exercise 4
# 
# Try to make a function called permutation that takes two numbers, n and r, and returns
# 
# n!/(n-r)! (! is the factorial symbol)

# ```{admonition} Click to show solution
# :class: dropdown
#         def permutation(n, r):
#             n_factorial = factorial(n)
#             n_r_factorial = factorial(n-r)
#             return (n_factorial/(n_r_factorial))
# ```

# Here is a function with no inputs, but still does something. This is useful if, for example, you want to print a lot of text every time something happens.

# In[110]:


def HelloWorld():
    print("Hello World!")


# In[111]:


HelloWorld()


# Let's say we want the factorials returned when we call the combination function. Although Python only allows one value to be returned from a function, we can bypass that by combining all the elements into a list

# In[112]:


def combination(n, r):
    n_factorial = factorial(n)
    r_factorial = factorial(r)
    n_r_factorial = factorial(n-r)
    return [n_factorial,r_factorial,(n_factorial/(r_factorial * n_r_factorial))]


# In[113]:


combination(14, 3)


# ## Exercise 5

# Try to print the multiplication table from 1 to 100, with 10 rows and 10 columns!

# ```{admonition} Click to show solution
# :class: dropdown
# 
#         for i in range(1, 11):
#             for j in range(1, 11):
#                 print(i*j, end = " ")
#             print("\n")
# ```

# ## Dictionaries

# Dictionaries in Python can be used to match certain values up. For example, if we had a list of employees with their names, emails, and phone numbers, we could use a dictionary for each employee to match up their name with a name variable, their email with an email variable, etc.

# We can define a dictionary as follows:
# 
#     <dictionary name> = {<variable name 1>:<variable 1 value>,....<variable name n>:<variable n value>}

# In[114]:


dict1 = {'Name':'John', 'Email':'johnsmith@gmail.com', 'Number':'918-029-0293'}


# In[115]:


dict1


# To reassign a value in the dictionary or to add a new value, simply type
#     
#     <dictionary name>[<name of key>] = <new value>

# In[116]:


dict1['Name'] = 'Mitch'


# In[117]:


dict1['Birthday'] = 'Jan 1 9182'


# In[118]:


dict1


# To view emojis in Python, we can install and load the emoji python

# In[119]:


get_ipython().system('pip install emoji')


# In[120]:


import emoji


# To print an emoji, we can type "emoji.emojize(\<text with emojis>, language = "alias")

# In[121]:


print(emoji.emojize(':smile:', language="alias"))
print(emoji.emojize("Python is :thumbsup:", language="alias"))


# To get the keys (the items corresponding to the definitions, but not the definitions themselves), we can use the keys() function

# In[122]:


dict1.keys()


# ## Exercise 6
# Ask the user for an input. If any of the words in this list are detected, replace them with emojis.
# 
# 
# 
# 
# Hint: Split the input for each word and check if the word is in the list from there

# In[123]:


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

# ## Dates

# To use dates, we can import the date module from the datetime package. 
# 
# First, we can define a function called printDate(). It will begin by printing the date today, which is shown by date.today().
# 
# To format the date, we can use the .strftime() function, as shown, to format it however you would like

# In[124]:


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


# In[125]:


date = printDate()


# In[126]:


print(date)


# Note that when we call printDate(), not only are the printed items in the function printed, but the returned value is shown after the "Out" text.

# In[127]:


printDate()


# ## Try and Except Statements

# Try and except statements can be used when you encounter an error, but want to do something with it instead of having Python deal with it.

# First, lets define a function called simpleMath which does some simple math

# In[128]:


def simpleMath(x, y):
    
    print("Multiplication: ", x*y)
    print("Addition: ", x + y)
    print("Subtraction: ", x-y)
    print("Division: ", x/y)


# In[129]:


simpleMath(4, 2)


# Note that if we put a string in place instead of a number, an error is given, as we cannot apply mathematical operations to strings

# In[130]:


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


# ## Classes

# Classes in Python can be used to create our own data types with their own functions

# Let's start by creating a class called Dog. With it, we can call the PrintDog function, which prints their name, age, and bark, as well as the isPuppy function, which prints whether or not the dog is a puppy. To initialize the class, we'll want to eneter in the dog's name, age, and bark. By setting bark = "Woof", if bark is not entered, the bark will, by default, be set to "Woof"

# In a class, we'll start with the \_\_init__ function, which initializes the variables in the class. We start with the self argument, which can be accessed by the rest of the class. The self argument is used to access the rest of the variables in the class. For example, self.name will represent the name. Next, we pass in the rest of the parameters -- name, age, and bark. We set the self values so that they can be accessed in other functions.
# 
# Next, we write the other functions, PrintDog and isPuppy

# In[135]:


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

# In[136]:


fido = Dog("Fido", 5)


# Notice how the default bark is Woof

# In[137]:


fido.printDog()


# We can also set a custom bark with Jack

# In[138]:


jack = Dog("Jack", 2, "arf")


# In[139]:


jack.printDog()


# ### Inheritance

# We can also create new classes based off the "parent" class, which can access the parent class's functions as well as new ones that are defined.
# 
# In this example, we are creating Labradoodle to be a child of the Dog class, which is shown by the Dog being in parenthesis. To initialzie the variables that are in both Labradoodle and Dog, we can use the super().\_\_init__ function, and initialize everything else like the Dog class.
# 
# Variables of the data type Labradoodle can access functions in both the Labradoodle and Dog class, while variables of the data type Dog can only access functions in the Dog class.

# In[140]:


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


# ## Hangman Exercise (Exercise 7)

# Remember how random.random() generates a number between 0 and 1. Similarly, if you wanted it to generate a number between 1 and 10, we could multiply that by 10. To make sure it goes up to 10 and is not less than 1, we use math.ceil() to round up, as shown:

# In[144]:


math.ceil(random.random() * 10)


# Here is a quick little code block that applies this to a guessing game. We generate a number, and the user tries to guess it. If the flag (guessed) is not True, we keep going until the user guesses correctly.

# In[145]:


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

# ## Files and Directories 

# To access and edit directories, we'll want to import the pre-installed os module

# In[149]:


import os


# To get a list of files in your current directory, we can type the listdir() command

# In[150]:


os.listdir()


# To obtain the file path of our current working directory, we can call the getcwd() command

# In[151]:


os.getcwd()


# To change our directory, we can enter the path of the new directory. It can either be relative to the directory at hand or to the computer as a whole

# In[157]:


os.chdir("/Users/schugani")


# In[158]:



os.chdir('Documents')
os.chdir('/Users/schugani')


# To create a folder, we can call the mkdir() function. This path should be relative to the computer.

# First, we can obtain our current directory path

# In[159]:


cur_path = os.getcwd()


# Next, we can name our new folder

# In[160]:


folder_name = "datasets"


# Finally, we can join the two with os.path.join and make a directory based on that

# Here, we can write a try except block that states that if the directory already exists, it will print so and the directory will not be created

# In[161]:


new_dir = os.path.join(cur_path, folder_name)
try:
    os.mkdir(new_dir)
except FileExistsError:
    print("file already exists")


# Let's say we have a file called data.csv and want to move it to our new directory. First, we want to move it to our current directory without Python. Next, we can use os.rename to change the path

# In[165]:


old_path = os.path.join(cur_path, "data.csv")
new_path = os.path.join(new_dir, "data.csv")
os.rename(old_path, new_path)


# In[166]:


os.chdir(new_dir)


# In[167]:


os.listdir()


# Nice! Now our data is in our new directory

# To change our directory back to the old one, we can call the chdir() function with the old path (that we saved as cur_path)

# In[168]:


os.chdir(cur_path)


# ## More Pandas 

# Let's create a data set with some names, ages, and heights

# In[169]:


names = ['John', 'Jeff', 'George']
ages = [12, 20, 34]
heights_ft = ["6'4", "5'7", "5'2"]

df = pd.DataFrame(list(zip(names, ages, heights_ft)))


# In[170]:


df.columns = ['Name', 'Age', 'Height (ft)']


# In[171]:


df


# First, we can convert the height column to two new columns -- feet and inches. This allows us to have the height as a combination of numbers instead of a string, enabling us to perform mathemetical operations on it

# In[172]:


df['Feet'] = [float(i[0]) for i in df['Height (ft)']]
df['In'] = [float(i[2:]) for i in df['Height (ft)']]


# Breaking down the code here, we have 
#      ```df['Feet'] = [float(i[0]) for i in df['Height (ft)']]```
# This says that we want to take float(i\[0]). This is the first element in i. Next, we have "for i in df\\['Height (ft)'\]", which means that each i represents a value in the Height (ft) column. Therefore, for each height, we are taking the first element. Since the height column is a string, this is the first character.
# 
# For inches, we do the same thing, except we take the third character and beyond (i\[2:]). We do this because the first character is the feet, the second character is a ', and everything beyond that is inches.
#     

# To create a new column for the height in centimeters, we can multiply the feet by 12 (because there are 12 inches in a foot) and then by 2.54 (because there are 2.54 cm per inch) and add that to the inches multiplied by 2.54. Something that's really cool about Pandas is that we can add columns like this without any loops or extra code.

# In[173]:


df['Height (cm)'] = df['Feet'] * 12 * 2.54 + df['In'] * 2.54


# In[174]:


df


# To subset data, we first need a list of True/False values that is equal to the length of the data set.

# In[175]:


df['Height (cm)'] > 170


# Then, we can just put that list inside the data frame!

# In[176]:


df[df['Height (cm)'] > 170]


# ## Exercise 8
# Find a subset of df for all people who have more than 3 inches in the 'In' part of their height! Save this to a dataframe called "edited_in"

# ```{admonition} Click to show solution
# :class: dropdown
# 
#         edited_in= df[df['In'] > 3]
# ```

# Similarly, we can do something for people who have less than 5 inches, like this:

# In[177]:


edited_in= df[df['In'] < 5]


# In[178]:


edited_in


# Note how for our edited_in data frame, the row indices go from 0 to 2. To reset this, we can call the reset_index() function

# In[179]:


edited_in.reset_index()


# Awesome! If we don't want our indices saved as a column, we can call the drop=True command from the reset_index function, like so:

# In[180]:


edited_in.reset_index(drop=True)


# However, note that this doesn't save the data frame

# In[181]:


edited_in


# To save the data frame with the resetted indices, we can call the inplace=True command

# In[182]:


edited_in.reset_index(drop=True, inplace=True)


# Alternatively, we could just set it equal to the data frame with the resetted indices

# In[183]:


edited_in = edited_in.reset_index(drop=True)


# In[184]:


edited_in 


# If we wanted to subset by more than one condition, we could incorporate the "&" (and) or "|" (or) symbols, putting each condition in parenthesis. To find all people with an age less than 20 and height more than 170 cm, we could write the following code:

# In[185]:


df[(df['Age'] < 20) & (df['Height (cm)'] > 170)]


# ## Machine Learning Project

# For this project, we'll be taking an online data set and trying to predict whether or not a person is biologically male or female given certain facial features. This data set is available at https://www.kaggle.com/datasets/elakiricoder/gender-classification-dataset 

# First, you'll want to download this data set and save it to your working directory as 'gender_classification_v7.csv'. Then, we can read it in as a pandas data frame called gender_df through the following command:

# In[186]:


gender_df = pd.read_csv('gender_classification_v7.csv')


# In[187]:


gender_df


# Great! Now, in order for Python to be able to read this a little easier, we can convert gender to a number. To do this, we can enter the following command:

# In[188]:


gender_df['gender_num'] = [0 if gender == "Female" else 1 for gender in gender_df['gender']]


# What this does is first assigns the output to a column in gender_df called gender_num.
# 
# Next, it states that for each gender in gender_df\['gender'], if it is female, we assign the corresponding value in gender_num to be 0. Otherwise, we assign it to be 1 (the "else 1" does this)

# In[189]:


gender_df


# Next, to train the model, we'll want to install and import the following two packages and modules.

# In[190]:


get_ipython().system('pip install numpy')
get_ipython().system('pip install scikit-learn')


# We'll use numpy to convert our data set into an array, and train_test_split to split our data into training and testing sets. This is important because we are utilizing a process called supervised learning.
# 
# Supervised learning is giving the computer data that tells it what's right and what's wrong, and based on that data, it asks it to predict new data. Training data is the data that tells the computer what to do, and testing data contains the computer's predictions. Based on its predictions, we can tell how accurate the model is, and deem whether or not it is good enough to predict new data not in the data set.

# In[191]:


import numpy as np
from sklearn.model_selection import train_test_split


# In[192]:


gender_df


# First, we'll want to split our data set into predictors and response. Our response is gender_num and our predictors are everything except gender and gender_num
# 
# We can convert our predictors and responses to arrays with the np.array command. Note that when we are selecting multiple columns from a data frame, we'll want to include double brackets.

# In[193]:


x = np.array(gender_df[['long_hair', 'forehead_width_cm', 'forehead_height_cm', 'nose_wide', 'nose_long',
                 'lips_thin', 'distance_nose_to_lip_long']])


# In[194]:


y = np.array(gender_df['gender_num'])


# Next, we can use the train_test_split function to split our data set up. Based on the x and y arrays, this splits it up into 4 variables. X_train and y_train contain the training set, and X_test and y_test contain the testing test. The test_size is 0.2, or 20% of our data, and random_state=42 just means that we have a different seed for randomization, enabling more consistent results.

# In[195]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# After that, we'll want to import tree from sklearn to train a decision tree. 
# 
# A decision tree uses a tree structure to determine the response. For example, it could say "if someone has long hair and brown eyes, they are a woman". We will visualize this later, so don't worry if you don't fully understand it now!

# In[196]:


from sklearn import tree


# We will want to set a variable with a name of our choice (in this case, clf) to a decision tree classifier to tell Python we want to use a decision tree. A decision tree is made up of a bunch of if statements -- for example, from our previous example of "if someone has long hair and brown eyes, they are a woman", there are 2 conditions for being a woman, with a depth of 2. Here, we can specify max_depth to be 3 to make this easier to visualize. 
# 
# We then fit this model on our training data

# In[197]:


clf = tree.DecisionTreeClassifier(max_depth = 3, random_state=42)
clf = clf.fit(X_train, y_train)


# Next, we can define the feature names (predictors) and class names (responses) to tell Python the names of the predictors and responses. Note that for class names, they are the names of each group of the response (male and female), not the name of the response itself (gender_num)

# In[198]:


feature_names = ['long_hair', 'forehead_width_cm', 'forehead_height_cm', 'nose_wide', 'nose_long',
                 'lips_thin', 'distance_nose_to_lip_long']
class_names = ['Female', 'Male']


# Using the export_text function imported from sklearn.tree, we can print our the tree rules. We can see, for example, that if distance_nose_to_lip_long <= 0.5 (meaning that if the distance from the subject's nose to lip is short), nose_wide <= 0.5 (the subject's nose is not wide), and forehead_width_cm <= 14.35 (the width of the subject's forehead, in cm, is <= 14.35), we predict that the subject is a woman.

# In[199]:


#import relevant functions
from sklearn.tree import export_text
#export the decision rules
tree_rules = export_text(clf,
                        feature_names = list(feature_names),
                        )
#print the result
print(tree_rules)


# To visualize this as a graph, we can import the graphviz package

# In[200]:


import graphviz 


# First, we'll want to define the data. We are using the clf model, with no file to save the graph to. The feature and class names have been defined. filled=True colors the boxed in and rounded=True makes the corners of the boxes round, 

# In[201]:


dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=feature_names,
                     class_names = class_names,
                     filled=True, rounded=True)  
graph = graphviz.Source(dot_data)  
graph 


# For each box, we are given a prediction. For example, if no information is given (the top box), we predict the subject to be male. However, the actual predictions given all the data come at the bottom row. Moving from the top down and to the left, if distance_nose_lip_long <= 0.5, nose_wide <= 0.5 and forehead_width_cm <= 14.35, we predict the subject to be female (as shown by class=Female). Moving to the right, if distance_nose_lip_long is not <= 14.35 (so distance_nose_lip_long > 14.35), nose_wide > 0.5, and nose_long > 0.5, we predict the subject to be male.

# To find the accuracy of these predictions, we can use the testing data. First, we set y_pred to the predicted values based on the X_test data using the predict() function. Next, we can obtain an accuracy score based on said predictions

# In[202]:


from sklearn.metrics import accuracy_score


# In[203]:


y_pred = clf.predict(X_test)
accuracy_score(y_test, y_pred)


# This means that we were correct on approximately 96.2% of our model's guesses, which is pretty good!

# Another form of machine learning is linear regression. Thinking of y=mx+b, this is essentially plotting a line of best fit, but for a lot more variables in this case.

# First, we'll want to import the LinearRegression module, fit the model on the training data, and predict based on the testing inputs.

# In[204]:


from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(X_train, y_train)
y_pred_lr = reg.predict(X_test)


# Next, we'll want to clean the data. Since the responses are either 0 or 1, it wouldn't make sense to have guesses outside of that range. Therefore, if the guess (i) is < 0, it is set to 0, otherwise it is kept. Next, if it is >1, it is set to 1 -- otherwise, it stays the same

# In[205]:


y_pred_lr = [0 if i < 0 else i for i in y_pred_lr]
y_pred_lr = [1 if i > 1 else i for i in y_pred_lr]


# In[206]:


print(y_pred_lr[:10])


# To analyze our results, we can't use the accuracy_score function as our guesses are continuous -- they don't always fall on 0 or 1. Thus, we will want to find the mean absolute error. For example, if the value is 1 and our guess is 0.95, our mean absolute error is abs(1-0.95) = 0.05. This is the same calculation as our accuracy score. If we subtract our mean absolute error from 1, we can get our approximate value for how many predictions we got right.

# In[207]:


from sklearn.metrics import mean_absolute_error


# In[208]:


1-mean_absolute_error(y_test, y_pred_lr)


# In[209]:


1-mean_absolute_error(y_test, y_pred)


# The linear regression model only has an accuracy of about 88.2%, so our decision tree model seems to fit better.
