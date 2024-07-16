## Second data type --> NUMBERS!

# Intergers - just a whole number
num1 = 200 # this is an intenger

# Float - a number with a  decimal value
num2 = 5.89
num3 = 5.00 # this is still a float

print("num1 data type:", type(num1))
print("num2 data type:", type(num2))
print("num3 data type:", type(num3))

new_num_string = str(num1)
print(new_num_string)
print(type(new_num_string))

# print(num1 + " This is a string") This will give us an error, we're trying to add a number to a string
print(str(num1) + " this is a number") # here we type cast the integer storeds in num1 as a string so we can concatenate it with other string

print('='*50) # this is just a divider line

new_thing = str(num2)
print(new_thing)
print("New thing data type: ", type(new_thing))

print('='*50)

# user_input = input("Enter a number here: ")
# print(user_input)
# print(type(user_input))

# # print(user_input + 25) # can't add a string (from input) and an integer
# print(int(user_input) + 25)

# user_input = int(input("Enter a number here: "))
# print(user_input, type(user_input))

print('='*50)

# Addition +
add_this = 10 + 25
print(add_this)

# Subtraction -
subtract_this = 100 - 25 - 1
print(subtract_this)

# Mulitplication *
multiply_this = 10 * 100
print(multiply_this)

# Division /
divide_this = 100 / 3
print(divide_this)

# Modulo %
remainder = 100 % 3
print(remainder)

num1 = 50
is_even = num1 % 2
print(is_even)

is_odd = 7 % 2
print(is_odd)

# Exponents  num ** exponent
raise_this = 10 ** 2
print(raise_this)

# PEMDAS
ex = (5 + 5) ** (2 + 2) - (3 / 4)
print(ex)

ex2 = 5 + 5 ** (2 + 2) - (3 / 4)
print(ex2)