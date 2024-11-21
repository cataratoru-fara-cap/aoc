
def compare_1(pulls, colors):
    ans = False
    for pull in pulls:
        for ball in pull.split(","):
            for number, color in colors:
                value = ""
                if color in ball:
                    for ch in ball:
                        if ch.isdecimal():
                            value += ch

                if value == "":
                    continue
                elif int(value) > number:
                    ans = True
                    return ans
    return ans


def sol_1(file):
    my_file = open(f"{file}", "r")
    lines = my_file.readlines()
    sum = 0

    for count, line in enumerate(lines, 1):
        n_line = line.split(":")
        pulls = n_line[1].split(";")
        colors = [(12, "red"), (13, "green"), (14, "blue")]
        ans = compare_1(pulls=pulls, colors=colors)

        if ans is False:
            sum += count

    return sum


print(sol_1("input2.txt"))


def compare_2(pulls, colors):
    for pull in pulls:
        for ball in pull.split(","):
            for color, num in colors.items():
                if color in ball:
                    k = ""
                    for ch in ball:
                        if ch.isdecimal():
                            k += ch
                    if int(k) > num:
                        colors[f"{color}"] = int(k)

    return colors


def sol_2(file):
    my_file = open(f"{file}", "r")
    lines = my_file.readlines()
    sum = 0

    for line in lines:
        colors = {"red": 0, "blue": 0, "green": 0}
        n_line = line.split(":")
        pulls = n_line[1].split(";")
        results_dict = compare_2(pulls=pulls, colors=colors)

        pow = results_dict["red"] * results_dict["green"] * results_dict["blue"] # noqa
        sum += pow

    return sum


print(sol_2('input2.txt'))
