from collections import defaultdict


def calculate_anti_nodes(node1: tuple, node2: tuple, len_mat: (int, int) ):
    global my_set
    x1, y1 = node1
    x2, y2 = node2
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    len_x, len_y = len_mat

    if x2 > x1:
        anti_x_1 = x2 + dx
        anti_x_2 = x1 - dx
    elif x2 < x1:
        anti_x_1 = x2 - dx
        anti_x_2 = x1 + dx

    if y2 > y1:
        anti_y_1 = y2 + dy
        anti_y_2 = y1 - dy
    elif y2 < y1:
        anti_y_1 = y2 - dy
        anti_y_2 = y1 + dy

    if (0 <= anti_x_1 < len_x) and (0 <= anti_y_1 < len_y):
        my_set.add((anti_x_1, anti_y_1))
    if (0 <= anti_x_2 < len_x) and (0 <= anti_y_2 < len_y):
        my_set.add((anti_x_2, anti_y_2))


mat = [line.strip() for line in open("input.txt").readlines()]
len_mat = (len(mat), len(mat[0]))
symbols = defaultdict(list)
my_set = set()

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] != '.':
            symbols[mat[i][j]].append((i, j))

for values in symbols.values():
    for node1 in values:
        for node2 in values:
            if node1 == node2:
                continue
            else:
                calculate_anti_nodes(node1, node2, len_mat)

print(len(my_set))