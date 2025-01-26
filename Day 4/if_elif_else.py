# if statement
# syntax 
condition = True
if condition:
    # code to execute is condition is true
    pass

# example
age = 18
if age >= 18:
    print("You are an adult.")
    

# elif statement
# syntax
condition1, condition2 = ''
if condition1:
    # code to execute if condition1 is True
    pass
elif condition2:
    # code to execute if condition2 True
    pass

# example
age = 15 
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print('You are a teenager.')
    

# else statement
# synatax
if condition1:
    # code to execute if condition1 is True
    pass
elif condition2:
    # code to execute if condition2 True
    pass
else:
    # code to execute if all conditions are false
    pass

# example
age = 10
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print('You are a teenager.')
else:
    print('You are a child.')