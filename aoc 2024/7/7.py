from math import log10

equations = (list(map(int, line.replace(':', ' ').split())) for line in open("demo.txt"))


def digits(n: int) -> int:
    return int(log10(n)) + 1

# this function is broken and I don t know why
def endswith(test_value: int, num: int) -> bool:
    return (test_value - num % 10) % 10 == 0


def valid_eq(test_value: int, numbers: list[int]) -> int:
    results = [numbers[0]]
    for num in numbers[1:]:
        temp = []
        for result in results:
            temp.append(result + num)
            temp.append(result * num)
            # only line for part two
            # temp.append(int(f"{result}{num}"))
        results = temp

    if test_value in results:
        return test_value
    return 0


sum = 0
for eq in equations:
    test_value, *numbers = eq
    # if not (endswith(test_value, numbers[-1]) or (test_value % numbers[-1] == 0)):
    #     continue
    sum += valid_eq(test_value, numbers)

print(sum)