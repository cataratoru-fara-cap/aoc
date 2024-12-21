import re

file = open("input.txt").readlines()
robots = [tuple(map(int, re.findall(r'(-?\d+)', robot))) for robot in file]
width = 101
length = 103 
bathroom = [['.' for j in range(width)] for i in range(length)]
def calculate_positions(x: int, y:int, dx:int, dy:int) -> list[tuple[int, int]]:
    cur = (x,y)
    positions = [cur]
    while True:
        x = (x + dx) % width
        y = (y + dy) % length
        cur = (x, y)
        if cur in positions:
            break
        positions.append(cur)
        
    return positions

for robot in robots:
    positions = calculate_positions(*robot)
    pos_100 = 100 % len(positions)
    j, i = positions[pos_100]
    if bathroom[i][j] == '.':
        bathroom[i][j] = 1
    else:
        bathroom[i][j] += 1

lu, ru, ld, rd = 0, 0, 0, 0
for i in range(length):
    for j in range (width):
        if bathroom[i][j] == '.':
            continue
        elif i < (length - 1)/2  and j < (width - 1)/2 :
            lu += bathroom[i][j]
        elif i < (length - 1)/2  and j > (width - 1)/2 :
            ru += bathroom[i][j]
        elif i > (length - 1)/2  and j < (width - 1)/2 :
            ld += bathroom[i][j]
        elif i > (length - 1)/2  and j > (width - 1)/2 :
            rd += bathroom[i][j]

print(lu * ru * ld * rd)
