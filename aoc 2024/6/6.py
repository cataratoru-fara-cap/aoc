import winsound

def find_guard(file: list) -> tuple[int, int]:
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] == "^":
                return (i, j)


def move_left() -> None:
    global marks, y, x
    x -= 1
    marks[y][x] = "<"


def move_up() -> None:
    global marks, y, x
    y -= 1
    marks[y][x] = "^"


def move_right() -> None:
    global marks, y, x
    x += 1
    marks[y][x] = ">"


def move_down() -> None:
    global marks, y, x
    y += 1
    marks[y][x] = "v"

def read_input(name: str) -> list:
    file = open(name, "r")
    file = [[char for char in line.strip()] for line in file.readlines()]
    return file


# part1
# y, x = find_guard(file)

# command = "up"
# while (True):
#     marks[y][x] = 'X'
#     if (y == 0 or x == 0 or
#         (y == len(file) - 1) or
#             (x == len(file) - 1)):
#         break

#     match command:
#         case "up":
#             if marks[y-1][x] != "#":
#                 move_up()
#             else:
#                 command = "right"
#         case "right":
#             if marks[y][x + 1] != "#":
#                 move_right()
#             else:
#                 command = "down"
#         case "down":
#             if marks[y+1][x] != "#":
#                 move_down()
#             else:
#                 command = "left"
#         case "left":
#             if marks[y][x-1] != "#":
#                 move_left()
#             else:
#                 command = "up"
#         case _:
#             print("Unknown command")

# sum1 = 0
# for line in marks:
#     for mark in line:
#         if mark == "X":
#             sum1 += 1

# print(sum1)
# part 2
file = read_input("demo.txt")
loc = find_guard(file)
sum2 = 0
for i in range(len(file)):
    for j in range(len(file[i])):
        marks = read_input("demo.txt")
        command = "up"
        visited = [0, 0, 0, 0]
        y, x = loc
        if marks[i][j] != "#" and marks[i][j] != "^":
            marks[i][j] = "#"
            pos = (i, j)
        else:
            continue

        while (True):
            marks[y][x] = 'X'
            if (y == 0 or x == 0 or
                (y == len(file) - 1) or
                    (x == len(file) - 1)):
                break

            match command:
                case "up":
                    if marks[y-1][x] != "#":
                        move_up()
                    elif (y-1, x) == pos:
                        visited[0] += 1
                        command = "right"
                    else:
                        command = "right"
                case "right":
                    if marks[y][x + 1] != "#":
                        move_right()
                    elif (y, x+1) == pos:
                        visited[1] += 1
                        command = "down"
                    else:
                        command = "down"
                case "down":
                    if marks[y+1][x] != "#":
                        move_down()
                    elif (y+1, x) == pos:
                        visited[2] += 1
                        command = "left"
                    else:
                        command = "left"
                case "left":
                    if marks[y][x-1] != "#":
                        move_left()
                    elif (y, x-1) == pos:
                        visited[3] += 1
                        command = "up"
                    else:
                        command = "up"
                case _:
                    print("Unknown command")

            if 2 in visited:
                sum2 += 1
                break

print(sum2)


def play_sound():
    frequency = 1000  # Set Frequency To 1000 Hertz
    duration = 1000   # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


play_sound()