# iterates over keys, values,or both
my_dict = {'a': 1,
           'b': 2,
           'c': 3
            }

# Iterate over keys
for key in my_dict:
    print(key)
    
    
# Iterate over values
for value in my_dict.values():
    print(value)
    
    
# Iterate over key-value pairs

for key, value in my_dict.items():
    print(key,value)