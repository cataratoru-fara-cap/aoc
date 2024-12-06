import re


file = open("input.txt", 'r').read()

#part 1


def mul(x, y)-> int:
    return x*y


finds1 = re.findall(r"mul\(\d{1,3},\d{1,3}\)", file)
print(finds1)

sum1 = 0
for x in finds1:
    sum += eval(x)

print(sum1)

#part2
mul_str = r"mul\(\d{1,3},\d{1,3}\)"
do_str = r"do\(\)"
dont_str = r"don't\(\)"
combined_regex = f"({mul_str}|{do_str}|{dont_str})"
finds2 = re.findall(combined_regex, file)
# print(finds2)

sum2 = 0
do = True
for x in finds2:
    if x == "don't()":
        do = False
    elif x == "do()":
        do = True
    elif do == True:
        sum2 += eval(x)
        
print(sum2)