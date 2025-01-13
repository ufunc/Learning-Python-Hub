# I plan to dominate for loops here from basics to advanced
# Each steps will be covered from loop1  to ...

# Basic Syntax:
variable = ''
iterable = ''

for variable in iterable:
    # code block to execute
    pass

# Example:
fruits = ['apple','banana', 'cherry']
for fruit in fruits:
    print(fruit)
    
'''
Here, fruit is the variable and fruits is the iterable
- A variable is a temporary variable that takes the value of each element in the iterable
Think of it like assigning a value to a variable but here the for loop assigns it and it is temporary.
- An iterable is an object that can return it's elements one at a time (e.g list, string, tuple, or range.)
Think of it as an object that stores multiple values in which the for loop brings out these values one at a time to a variable
'''