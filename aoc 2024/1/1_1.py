with open("input.txt", 'r') as file:
    file = file.readlines()
first_pos = []
second_pos = []
result = 0

for line in file:
    args = line.split()
    first_pos.append(int(args[0]))
    second_pos.append(int(args[1]))

first_pos.sort()
second_pos.sort()

for pair in zip(first_pos, second_pos):
    result += abs(pair[0] - pair[1])

print(result)