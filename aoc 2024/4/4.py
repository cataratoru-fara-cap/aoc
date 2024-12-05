import numpy as np

file = open("demo.txt","r")
file = file.read().splitlines()

def compare(my_list: str) -> int:
    res = 0
    for i in range(len(my_list) - 3):
        if my_list[i:i+4] == "XMAS":
            res += 1
    return res

def get_diagonals(matrix):
    diagonals = []
    np_matrix = np.array(matrix)
    rows, cols = np_matrix.shape

    for offset in range(-rows + 1, cols):
        diagonal = np.diagonal(np_matrix, offset=offset)
        diagonals.append(diagonal.tolist())
    
    return diagonals


rows = file
rows_reverse = [''.join(reversed(string)) for string in file]

columns = [[char for char in line] for line in file]
columns = np.array(columns).T
columns = [''.join(list )for list in columns]
columns_reverse = [''.join(reversed(string)) for string in columns]

diagonals = get_diagonals([[char for char in line] for line in file])
diagonals = [''.join(line) for line in diagonals]
diagonals_reverse = [''.join(reversed(string)) for string in diagonals]

# print("Rows:", rows)
# print("Reversed Rows:", rows_reverse)
# print("Columns:", columns)
# print("Reversed Columns:", columns_reverse)
# print("Diagonals:", diagonals)
# print("Reversed Diagonals:", diagonals_reverse)
to_compare = [rows, rows_reverse, columns, columns_reverse, diagonals, diagonals_reverse]
sum = sum(sum([compare(line) for line in text]) for text in to_compare)
print(sum)
