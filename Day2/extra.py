mov = input("Insert the submarine's movements below:\n")
mov_lst = mov.split(' ')

x = 0
aim = 0
depth = 0

for item in mov_lst:
    try:
        distance = int(item)
        if(order == 'forward'):
            x += distance
            depth += (aim * distance)
        elif(order == 'down'):
            aim += distance
        elif(order ==  'up'):
            aim -= distance
    except:
        order = item.lower()

result = x * depth
print(f'\nDepth={depth}\nHorizontal={x}\nResult={result}')