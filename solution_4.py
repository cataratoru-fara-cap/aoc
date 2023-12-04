from collections import defaultdict


def solution_1(file):
    # modifing input
    my_file = open(file)
    lines = my_file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(":")[1]
        lines[i] = lines[i].split("|")

        lines[i][0] = set(lines[i][0].split())
        lines[i][1] = lines[i][1].split()

    sum = 0
    for line in lines:
        ans = 0
        i = 0
        for wn in line[0]:
            if wn in line[1]:
                i += 1

        if i != 0:
            ans = pow(2, i-1)

        sum += ans

    return sum


print(solution_1("input4.txt"))


def solution_2(file):
    # modifing input
    my_file = open(file)
    lines = my_file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(":")[1]
        lines[i] = lines[i].split("|")

        lines[i][0] = set(lines[i][0].split())
        lines[i][1] = lines[i][1].split()

    sum = 0
    my_dict = defaultdict(lambda: 1)
    for i, line in enumerate(lines, 1):
        c = 0
        for wn in line[0]:
            if wn in line[1]:
                c += 1

        for j in range(c):
            my_dict[i+1+j] += my_dict[i]

        sum += my_dict[i]

    return sum


print(solution_2("input4.txt"))