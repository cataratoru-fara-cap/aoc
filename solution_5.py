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


seeds = [int(i) for i in list(processed_data_dict.values())[0][0]]
locations_1 = []
for loc in seeds:  # gets the seed values
    seed_dest = locator(int(loc))
    locations_1.append(seed_dest)

# print(locations_1)
#print(min(locations_1))

locations_2 = []
i = 0
j = 1

while (j <= len(seeds) - 1):
    for k in range(seeds[i], seeds[i] + seeds[j]):
        seed_dest = locator(k)
        locations_2.append(seed_dest)
    i += 2
    j += 2

# print(locations_2)
print(min(locations_2))
