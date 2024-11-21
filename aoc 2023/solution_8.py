def parser(my_file):
    my_map = {}
    with open(f"{my_file}") as file:
        directions = file.readline().strip()
        lines = file.read().strip().replace(" ", "").split("\n")
        for line in lines:
            key, value = line.split("=")
            right, left = value.replace("(", "").replace(")", "").split(",")
            my_map[key] = (right, left)

    return my_map, directions


my_map, directions = parser("input8.txt")
# for k, v in my_map.items():
#     print(k, v)
# print(directions)


def proceser(my_count=1, my_key="AAA"):
    counter = my_count
    key = my_key
    for i in directions:
        match i:
            case "R":
                d = 1
            case "L":
                d = 0
            case _:
                raise LookupError

        if my_map[key][d] == "ZZZ":
            return counter

        key = my_map[key][d]
        counter += 1

    return proceser(my_count=counter, my_key=key)


# print(proceser())

my_map, directions = parser("input8.txt")
start_keys = [key for key in my_map.keys() if key[2] == "A"]


def proceser2(my_count=1, start_keys=start_keys):
    counter = my_count
    keys = start_keys
    while True:
        for i in directions:
            match i:
                case "R":
                    d = 1
                case "L":
                    d = 0
                case _:
                    raise LookupError

            k = 0
            for key in keys:
                if my_map[key][d][2] == "Z":
                    k += 1

            if k == len(keys):
                break

            for i, key in enumerate(keys):
                keys[i] = my_map[key][d]

            counter += 1


print(proceser2())
