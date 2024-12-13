
def blink(stones: list[str]) -> list[str]:
    new_line = []
    for stone in stones:
        if stone == "0":
            new_line.append("1")
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left = stone[:mid]
            right = stone[mid:].lstrip('0') or '0'
            new_line.append(left)
            new_line.append(right)
        else:
            new_line.append(f"{int(stone) * 2024}")

    return new_line


stones = open("input.txt").read().split()
for _ in range(26):
    new_stones = blink(stones)
    stones = new_stones

print(len(stones))