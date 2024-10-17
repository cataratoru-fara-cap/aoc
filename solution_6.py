def parser(file):
    file = open(f"{file}", "r").read().split("\n")
    distances_times = [row.split(":")[1].split(" ") for row in file]
    times, distances  = [[int(num) for num in nums if num != ""]
                        for nums in distances_times]
    return times, distances
    # print(speed, time)

def parser2(file):
    file = open(f"{file}", "r").read().split("\n")
    times, distances = [[int(row.split(":")[1].replace(" ", ""))]
                        for row in file]
    return times, distances


times, max_distances = parser("input6.txt")
times2, max_distances2 = parser2("input6.txt")

def solver(times, max_distances):
    ans = 0
    for i in range(len(max_distances)):
        ways_to_win = 0
        for bhdwn in range(times[i]):
            distance = bhdwn * (times[i] - bhdwn)
            if distance > max_distances[i]:
                ways_to_win += 1

        if ways_to_win != 0:
            if ans == 0:
                ans = 1
            ans *= ways_to_win

    return ans


print(solver(times, max_distances))
print(solver(times2, max_distances2))
