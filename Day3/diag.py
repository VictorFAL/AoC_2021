diag = input('Insert the diagnostic repost below:\n')
diag_lst = diag.split(' ')

gamma = []
epsilon= []

index = 0
bit = 0
bit_lst = []
while(bit < len(diag_lst[0])):
    bit_lst.append(diag_lst[index][bit])
    index +=1
    if(index == len(diag_lst)):
        # appending most common bit to gamma list & least common to epsilon
        gamma.append(max(bit_lst, key=bit_lst.count))
        epsilon.append(min(bit_lst, key=bit_lst.count))

        index = 0
        bit += 1
        bit_lst = []

# joining both lists to form a binary string
gamma = ''.join(gamma)
epsilon = ''.join(epsilon)

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

result = gamma * epsilon
print(f'The power consumption of the submarine is of {result}')