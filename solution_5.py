file = open("input5.txt", "r").read().split("\n\n")
processed_data_dict = {}
for i in range(len(file)):
    key, codes = file[i].strip().split(":")
    codes = [item.split() for item in codes.split("\n") if item != ""]
    processed_data_dict[key] = codes

for k, v in processed_data_dict.items():
    print(k, v)


def locator(seed):
    curNum = seed
    for values in list(processed_data_dict.values())[1:]:  # noqa excluedes seeds from parsing
        for lst in values:
            d_start, src_start, r = int(lst[0]), int(lst[1]), int(lst[2])
            if src_start <= curNum < src_start + r:
                curNum = d_start + (curNum - src_start)
                break
    return curNum


locations = []
for loc in list(processed_data_dict.values())[0]:  # gets the seed values
    for sub_loc in loc:  # loc is a list of lists with values
        seed_dest = locator(int(sub_loc))
        locations.append(seed_dest)

print(locations)
print(min(locations))
