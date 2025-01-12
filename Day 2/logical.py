# and  (Logical AND)
# Returns True if both conditions are True
x = 5
y = 10
(x > 3 and y < 15)  # True (both conditions are True)
(x > 6 and y < 15)  # False (first condition is False)

# or (Logical OR)
# Returns True if at least one condition is True
x = 5
y = 10
(x > 3 or y > 15)  # True (first condition is True)
(x > 6 or y > 15)  # False (both conditions are False)

# not (Logical Not)
# Reverses the result of a condition
# True becomes False
# False becomes True
x = 5
not (x > 3)  # False (because x > 3 is True, and `not` negates it)
not (x < 3)  # True (because x < 3 is False, and `not` negates it)

# Use cases
# Logical operators are often used in if statements and loops for decision-making:
x = 7
if x > 5 and x < 10:
    print("x is between 5 and 10")



