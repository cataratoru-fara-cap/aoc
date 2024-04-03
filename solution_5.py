file = open("demo5.txt", "r").read().split("\n\n")
processed_data_dict = {}
for i in range(len(file)):
    key, codes = file[i].strip().split(":")
    codes = [tuple(int(i) for i in item.split()) for item in codes.split("\n") if item != ""]  # noqa
    processed_data_dict[key] = codes

raw_seeds = [i for i in list(processed_data_dict.values())[0][0]]
processed_data_dict["seeds"] = raw_seeds

# for k, v in processed_data_dict.items():
#     print(k, v)


def locator(seed):
    curNum = seed
    for values in list(processed_data_dict.values())[1:]:  # noqa excluedes seeds from parsing
        for lst in values:
            d_start, src_start, r = lst[0], lst[1], lst[2]
            if src_start <= curNum < src_start + r:
                curNum = d_start + (curNum - src_start)
                break
    return curNum


locations_1 = []
for loc in raw_seeds:  # gets the seed values
    seed_dest = locator(int(loc))
    locations_1.append(seed_dest)

# print(locations_1)
# print(min(locations_1))

processed_data_dict["seeds"] = [(raw_seeds[i], raw_seeds[i+1])
                                for i in range(0, len(raw_seeds), 2)
                                ]

seeds = processed_data_dict["seeds"]
maps = list(processed_data_dict.values())[1:]

print(seeds, "\n", maps)
