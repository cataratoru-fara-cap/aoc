from collections import defaultdict
from functools import cmp_to_key


def parser(file):
    my_txt = open(f"{file}").readlines()
    my_hands = [tuple(line.strip().split(" ")) for line in my_txt]
    my_hands = [(hand[0], int(hand[1])) for hand in my_hands]
    return my_hands


def get_type(hand):
    counts = defaultdict(int)
    for x in hand:
        counts[x] += 1

    amount = sorted(counts.values())
    match amount:
        case [5]:
            return 5
        case [1, 4]:
            return 4
        case [2, 3]:
            return 3.5
        case [1, 1, 3]:
            return 3
        case [1, 2, 2]:
            return 2.5
        case [1, 1, 1, 2]:
            return 2
        case _:
            return 1


labels = "23456789TJQKA"


def compare(a, b):
    rankA = get_type(a)
    rankB = get_type(b)

    if rankA == rankB:
        for i, j in zip(a, b):
            if labels.index(i) > labels.index(j):
                return 1
            elif labels.index(i) < labels.index(j):
                return -1
        raise IndexError
    elif rankA >= rankB:
        return 1
    return -1


lines = parser("input7.txt")
lines = sorted(lines, key=cmp_to_key(lambda x, y: compare(x[0], y[0])))

ans = 0
for count, line in enumerate(lines, 1):
    print(line[0], count)
    ans += line[1] * count
print(ans)
