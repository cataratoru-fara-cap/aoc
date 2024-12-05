with open("input.txt", 'r') as file:
    file = file.readlines()
first_pos = []
second_pos = []
result = 0

for line in file:
    args = line.split()
    first_pos.append(int(args[0]))
    second_pos.append(int(args[1]))

for i in first_pos:
    n = second_pos.count(i)
    result += i * n

print(result)