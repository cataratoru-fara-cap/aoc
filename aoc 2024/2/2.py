file = open("demo.txt",'r')
lines = file.readlines()
lines = [[int(x) for x in line.split()] in line for line in lines]
result = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])

def asc_cond(first, second) -> bool:
    if (first - second <= 3) and (first - second > 0):
        return True
    return False

def desc_cond(first, second) -> bool:
    if (second - first <= 3) and (second - first > 0):
        return True
    return False

#Part 1
"""for line in lines:
    #descending conditional
    if (line[0] - line[1] <= 3) and (line[0] - line[1] > 0):
        for i in range(1, len(line) - 1):
            if not ((line[i] - line[i+1] <= 3) and (line[i] - line[i+1] > 0)):
                break 
            elif i == len(line) - 2:
                result += 1     
    #ascending conditional
    elif (line[1] - line[0] <= 3) and (line[1] - line[0] > 0):
        for i in range(1, len(line) - 1):
            if not ((line[i+1] - line[i] <= 3) and (line[i+1] - line[i] > 0)):
                break
            elif i == len(line) - 2:
                result += 1 """      

def is_safe(row):
    inc = [row[i+1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {1, 2, 3}:
        return True
    return False
    

print(result)