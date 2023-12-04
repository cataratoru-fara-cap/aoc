def solution_1(file):
    #modifing input
    my_file = open(file)
    lines = my_file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(":")[1]
        print(lines[i])


solution_1("demo4.txt")
