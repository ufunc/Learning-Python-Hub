# basic syntax
condition = ''
while condition:
    # code to execute
    pass
    
# example
count = 0
while count < 5:
    break # i dont want this to run.
    print(f'Count is {count}')
    count += 1
    
# key concepts
# 1. infinite loops
while True:
    break # i dont want this to run
    print('This will run forever!')
    
    
# 2. breaking out of a loop
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break # used to break out of  for loop
    print(f"You entered: {user_input}")
    

# 3. skipping iterations
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(f"Count is {count}")
    
    
# nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1    
    

# why-else
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
else: # this executes when the loop condition becomes false
    print("Loop finished")
    
    
# use cases
# 1. user input validation
while True:
    age = input("Enter your age: ")
    if age.isdigit() and int(age) > 0:
        print(f"Your age is {age}.")
        break
    else:
        print("Invalid input. Please enter a positive number.")
    
# 2. game loops
game_over = False
while not game_over:
    user_input = input('What do you want to do? (quit/play): ')
    if user_input == 'quit':
        game_over = True
    else:
        print("Plating the game...")
    
# 3. processinng data
data = [1, 2, 3, 4, 5]
index = 0
while index < len(data):
    print(data[index])
    index += 1
    