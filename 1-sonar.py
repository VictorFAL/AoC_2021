report = input('Insert the sonar report below:\n')

# Converting input string to a list
lst = report.split(' ')
lst = list(map(int, lst))

increases = 0
for index in range(1, len(lst)):
    if(lst[index] > lst[index-1]):
        increases += 1

print(f'\nThere were {increases} increases of measurements in the given report.')