# The else runs if the loop finishes without encountering a break

for i in range(5):
    if i == 3:
        break
else:
    print('Loop completed!') # This wount run because the loop did not complete