from collections import defaultdict


def calculate_anti_nodes(node1: tuple, node2: tuple, len_mat: tuple[int, int]):
    global my_set
    x1, y1 = node1
    x2, y2 = node2
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    len_x, len_y = len_mat
    anti_x_1, anti_x_2, anti_y_1, anti_y_2 = x1, x2, y1, y2

    my_set.add(node1)
    my_set.add(node2)
    while (True):
        if x2 > x1:
            anti_x_1 -= dx
        else:
            anti_x_1 += dx

        if y2 > y1:
            anti_y_1 -= dy
        else:
            anti_y_1 += dy

        if not (0 <= anti_x_1 < len_x and 0 <= anti_y_1 < len_y):
            break
        my_set.add((anti_x_1, anti_y_1))

    while (True):
        if x2 > x1:
            anti_x_2 += dx
        else:
            anti_x_2 -= dx

        if y2 > y1:
            anti_y_2 += dy
        else:
            anti_y_2 -= dy

        if not (0 <= anti_x_2 < len_x and 0 <= anti_y_2 < len_y):
            break
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
            if node1 == node2 or len(values) == 1:
                continue
            else:
                calculate_anti_nodes(node1, node2, len_mat)

print(my_set)
print(len(my_set))