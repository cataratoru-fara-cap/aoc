from functools import cmp_to_key


file = open("input.txt", "r")

file = file.readlines()
for i in range(len(file)):
    if file[i] == '\n':
        rules = [rule.strip() for rule in file[:i]]
        page_numbers = [pg_num.strip().split(',') for pg_num in file[i+1:]]

# rules = [tuple(map(int, rule)) for rule in rules]
# page_numbers = [tuple(map(int, pg_num)) for pg_num in page_numbers]

print(rules, "\n\n", page_numbers, "\n\n")

cmp = cmp_to_key(lambda x, y: 1 - 2*(x + '|' + y in rules))
# Part 1
sum1 = 0
for page in page_numbers:
    sorted_page = sorted(page, key=cmp)
    if page == sorted_page:
        sum1 += int(page[(len(page)//2)])
print(sum1)

# Part 2
sum2 = 0
for page in page_numbers:
    sorted_page = sorted(page, key=cmp)
    if page != sorted_page:
        sum2 += int(sorted_page[(len(sorted_page)//2)])
print(sum2)