# Week 1 day 1 Lecture

# This is a comment
# Using a # allows you to write a comment in your code that will not be run. Python and VS Code will ignore it

# Our first line of code
print("Hello world!")

# This is a variable with a string stored in it
# A string is a data type used for storing text
first_words = "Hellow World!"

print(first_words)

# Here is a string with single quotes. It is still a string data type
new_string = 'I can also use single quotes'

# Escape charatcer \ allows us to still use single quotes inside of a single quote string
example = 'I can\'t use single quote\'s inside of single quote\'s'
print(example)

# Concatenating strings together - combine multiple strings together
string1 = "This is"
string2 = "super cool!"

# Concatenated multiple strings together and stored them in a new variable
concat = string1 + string2
print(concat)

# Concatenated two strings together using a + sign
print(string1 + string2)

print(string1 + " " + string2) # Concatenated with a "space string" added in

print(string1, string2) # Concatenated with a comma , will automatically add a space between my strings

# Docstring - a multiline string

### Incorrect format for a doc string (a multi line string)
# another_string = "
# line1
# line2
# line3
# "

# initiate a docstring with triple quotes, either single ''' or double """
doc = '''
Enter 1 to continue
Enter 2 to go back
Enter 3 to figure it all out
'''
print(doc)

# Python reads code from the top to the bottom, we've defined the variable doc, if we redefine the data stored there, then our print function will print that new piece of data
doc = "This is a new thing"

print(doc)

# Unpacking - We can define multiple pieces of data at once, and upack them positionally into their own variable(places in memory)
first, middle, last = "Travis", "Cline", "Peck"
print(middle)

print(first, middle, last)

# Never create a variable with a reserved word

# global = "this"
# if = "that"

# Global and If are both words that are already reserved for something else in Python

# print = "something here"
# print(print)