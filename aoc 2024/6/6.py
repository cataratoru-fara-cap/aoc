import winsound


def find_guard(file: list) -> tuple[int, int]:
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] == "^":
                return (j, i) #return x, y


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


# file = open("input.txt", "r")
# file = [[char for char in line.strip()] for line in file.readlines()]
# marks = file

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
area = open("input.txt").readlines()
loc = find_guard(area)
steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]
total = 0
x_start, y_start = loc[0], loc[1]
x, y, direction, locations = x_start, y_start, 0, set()
#compute the original path
while True:
    locations.add((x, y))
    x1, y1 = x + steps[direction][0], y + steps[direction][1]
    if not (0 < x1 < 130 and 0 <= y1 < 130):
        break
    if area[y1][x1] == "#":
        direction = (direction + 1) % 4
    x, y = x + steps[direction][0], y + steps[direction][1]

#only try to start infinete loops on the original path
for location in locations:
    x, y, direction, visited = x_start, y_start, 0, set()
    while True:
        if (x, y, direction) in visited:
            total += 1
            break
        visited.add((x, y, direction))
        x1, y1 = x + steps[direction][0], y + steps[direction][1]
        if not (0 < x1 < 130 and 0 <= y1 < 130):
            break
        if area[y1][x1] == "#" or (x1, y1) == location:
            direction = (direction + 1) % 4
        else:
            x, y = x + steps[direction][0], y + steps[direction][1]

print(total)


def play_sound():
    frequency = 1000  # Set Frequency To 1000 Hertz
    duration = 1000   # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


play_sound()