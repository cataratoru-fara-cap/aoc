
def sol_1():
    my_file = open(f"{file}", "r")
    lines = my_file.readlines()

    for line in lines:
        n_line = line.removeprefix("Game ").strip().split(":")
        index = int(n_line[0])
        pulls = n_line[1].replace(" ", "").split(";")
        colors = [(12, "red"), (13, "green"), (14, "blue")]

        for pull in pulls:
            for ball in pull.split(","):
                value = ""      
                for color, number in colors:
                    if color in ball:
                        for ch in ball:
                            if ch.isdecimal():
                                value += ch
                    if value > number:
                        break
