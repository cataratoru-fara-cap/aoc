data = open("input.txt").read().strip()
file = []
for i, value in enumerate(data):
    if i % 2 == 0:
        for j in range(int(value)):
            file += [int(i/2)]
    else:
        for j in range(int(value)):
            file += ['.']


i = 0
j = len(file) - 1

while (True):
    if i == j or j < i:
        break
    elif file[i] != '.':
        i += 1
    elif file[j] == '.':
        j -= 1
    elif file[i] == '.' and file[j] != '.':
        file[i] = file[j]
        file[j] = '.'
        i, j = i + 1, j - 1


sum = 0
for i, char in enumerate(file):
    if char == '.':
        break
    sum += i * int(char)

print(sum)

