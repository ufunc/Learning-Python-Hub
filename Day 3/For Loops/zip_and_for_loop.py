# Combine two or mre sequences and iterate over them simultanously 

names = ['Alice', 'Bob', 'Charlie']
scores = [90, 80, 70]

for name, score in zip(names, scores):
    print(f'{name} scored {score}')