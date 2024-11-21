from collections import defaultdict


def solution_1(my_file):
    file = open(f"{my_file}", 'r')
    lines = file.read().split("\n")
    G = [[c for c in line] for line in lines]
    R = len(G)
    C = len(G[0])
    ans = 0

    for r in range(len(G)):
        n = 0
        has_part = False
        for c in range(len(G[r]) + 1):
            if c < C and G[r][c].isdigit():
                n = n*10 + int(G[r][c])

                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if (0 <= r + rr < R) and (0 <= c + cc < C):
                            ch = G[r + rr][c + cc]
                            if not ch.isdigit() and ch != ".":
                                has_part = True

            elif (n > 0):
                # print(r, n, has_part)
                if has_part:
                    ans += n
                    has_part = False
                n = 0

    return ans


print(solution_1("input3.txt"))


def solution_2(my_file):
    file = open(f"{my_file}", 'r')
    lines = file.read().split("\n")
    G = [[c for c in line] for line in lines]
    R = len(G)
    C = len(G[0])
    ans = 0
    numbers = defaultdict(list)

    for r in range(len(G)):
        n = 0
        gears = set()
        for c in range(len(G[r]) + 1):
            if c < C and G[r][c].isdigit():
                n = n*10 + int(G[r][c])

                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if (0 <= r + rr < R) and (0 <= c + cc < C):
                            ch = G[r + rr][c + cc]
                            if ch == "*":
                                gears.add((r + rr, c + cc))

            elif (n > 0):
                # print(r, n, has_part)
                for gear in gears:
                    numbers[gear].append(n)
                n = 0
                gears = set()
    
    for value in numbers.values():
        if len(value) == 2:
            ans += value[0] * value[1]

    return ans


print(solution_2("input3.txt"))
