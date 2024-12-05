# part1
def star_search(chr: str, pos: tuple, size: tuple, mat: list) -> int:
    sum = 0
    y = pos[0]
    x = pos[1]
    if chr == 'X':
        if line(x, y, "left", size) and (mat[y][x-1] + mat[y][x-2] + mat[y][x-3] == "MAS"):
            sum += 1

        if line(x, y, "up", size) and (mat[y-1][x] + mat[y-2][x] + mat[y-3][x] == "MAS"):
            sum += 1

        if line(x, y, "right", size) and (mat[y][x+1] + mat[y][x+2] + mat[y][x+3] == "MAS"):
            sum += 1

        if line(x, y, "down", size) and (mat[y+1][x] + mat[y+2][x] + mat[y+3][x] == "MAS"):
            sum += 1

        if line(x, y, "dRightUp", size) and mat[y-1][x+1] + mat[y-2][x+2] + mat[y-3][x+3] == "MAS":
            sum += 1 

        if line(x, y, "dLeftUp", size) and mat[y-1][x-1] + mat[y-2][x-2] + mat[y-3][x-3] == "MAS":
            sum += 1 

        if line(x, y, "dRightDown", size) and mat[y+1][x+1] + mat[y+2][x+2] + mat[y+3][x+3] == "MAS":
            sum += 1 

        if line(x, y, "dLeftDown", size) and mat[y+1][x-1] + mat[y+2][x-2] + mat[y+3][x-3] == "MAS":
            sum += 1

    return sum


def line(x: int, y: int, orientation: str, size: tuple) -> bool:
    match orientation:
        case "left":
            return (x - 3 >= 0)
        case "up":
            return (y - 3 >= 0)
        case "right":
            return (x + 3 < size[1])
        case "down":
            return (y + 3 < size[0])
        case "dRightUp":
            return (x + 3 < size[1]) and (y - 3 >= 0)
        case "dLeftUp":
            return (x - 3 >= 0) and (y - 3 >= 0)
        case "dRightDown":
            return (x + 3 < size[1]) and (y + 3 < size[0])
        case "dLeftDown":
            return (x - 3 >= 0) and (y + 3 < size[0])
        case _:
            raise ValueError(
                "Invalid Orientation (righht/left/up/down/dRightUp/"
                "dLeftUp/dRightDown/dLeftDown)"
            )


# file = open("input.txt", "r")
# file = file.read().splitlines()
# file = [list(string) for string in file]

# part 1
# sum = 0
# for i in range(len(file)):
#     for j in range(len(file[i])):
#         sum += star_search(file[i][j], (i, j), (len(file), len(file[0])), file)
# print(sum)

# part 2


def x_search(chr: str, pos: tuple, size: tuple, mat: list) -> int:
    def diag() -> bool:
        if (mat[y-1][x+1] == "M" and mat[y+1][x-1] == "S") or \
           (mat[y+1][x-1] == "M" and mat[y-1][x+1] == "S"):
            return True
        return False

    def anti_diag() -> bool:
        if (mat[y-1][x-1] == "M" and mat[y+1][x+1] == "S") or \
           (mat[y+1][x+1] == "M" and mat[y-1][x-1] == "S"):
            return True
        return False

    y = pos[0]
    x = pos[1]
    if (mat[y][x] == "A" and diag() and anti_diag()):
        return 1
    return 0


file = open("input.txt", "r")
file = file.read().splitlines()
file = [list(string) for string in file]

sum2 = 0
for i in range(1, len(file)-1):
    for j in range(1, len(file[i])-1):
        sum2 += x_search(file[i][j], (i, j), (len(file), len(file[i])), file)
print(sum2)
