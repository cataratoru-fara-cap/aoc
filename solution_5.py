file = open("demo5.txt", "r").read().split("\n\n")
processed_data_dict = {}
for i in range(len(file)):
    key, codes = file[i].strip().split(":") 
    codes = [item.split() for item in codes.split("\n") if item != ""]
    processed_data_dict[key] = codes

for k,v in processed_data_dict.items():
    print(k, v)