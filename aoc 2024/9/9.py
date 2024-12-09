data = open("input.txt").read().strip()
my_str = ""

for i, file in enumerate(data):
    if i % 2 == 0:
        for j in range(int(file)):
            my_str += str(int(i/2))
    else:
        for j in range(int(file)):
            my_str += '.'

my_str = [char for char in my_str]
i = 0
j = len(my_str) - 1

while (True):
    if i == j or j < i:
        break
    elif my_str[i] != '.':
        i += 1
    elif my_str[j] == '.':
        j -= 1
    elif my_str[i] == '.' and my_str[j] != '.':
        my_str[i] = my_str[j]
        my_str[j] = '.'
        i, j = i + 1, j - 1


sum = 0
for i, char in enumerate(my_str):
    if char == '.':
        break
    sum += i * int(char)

print(sum)

