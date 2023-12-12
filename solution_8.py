my_map = {}

def parser(my_file):
    with open(f"my_file") as file:
        directions = file.readline()
        lines = file.read().replace(" ", "").split("\n")[1:]
        for line in lines:
            key, value = line.split("=")
            my_map[key] = value

# print(lines)
# for k, v in my_map.items():
#     print(k, v)

def proceser():
    pass
