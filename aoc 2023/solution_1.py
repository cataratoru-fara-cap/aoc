def solution1_1(file):
    my_file = open(f"{file}", "r")
    lines = my_file.readlines()
    ans = 0

    for line in lines:
        s1 = ""
        for ch in line:
            if ch.isdecimal():
                s1 += ch
        s1 = s1[0] + s1[-1]
        ans += int(s1)

    return ans


# print(solution1_1("input1.txt"))


def solution1_2(file):
    my_file = open(f"{file}", "r")
    lines = my_file.readlines()
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] # noqa
    ans = 0
    for line in lines:
        digits = []
        for i, ch in enumerate(line):
            if ch.isdecimal():
                digits.append(ch)
            for j, val in enumerate(nums, 1):
                if line[i:].startswith(val):
                    digits.append(str(j))
        coord = int(digits[0] + digits[-1])
        ans += coord

    return ans


print(solution1_2("input1.txt"))
