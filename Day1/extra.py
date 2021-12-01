report = input('Insert the sonar report below:\n')

# Converting input string to a int list
lst = report.split(' ')
lst = list(map(int, lst))

# creating a list with the results of the sums
sum_lst = []
for index in range(0, len(lst)):
    try:
        # assuring possibility of making a group of three
        assert index < len(lst)-2

        sum3 = sum(lst[index:index+3])
        sum_lst.append(sum3)
    except:
        break

increases = 0
for index in range(1, len(sum_lst)):
    if(sum_lst[index] > sum_lst[index-1]):
        increases += 1

print(f'\nThere were {increases} increases of sums in the given report.')