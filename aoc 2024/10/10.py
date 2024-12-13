M = [list(map(int, line.strip())) for line in open("input.txt").readlines()]

def dfs(matrix, start) -> int:
    stack = [start]
    directions = [(-1, 0), (0, -1), (+1, 0), (0, +1) ]
    reachable_9s = []
    while stack:
        row, col = stack.pop()
        if matrix[row][col] == 9:
            reachable_9s.append((row,col))
        else:
            for dx, dy in directions:
                nrow, ncol = row + dy, col + dx
                if 0 <= nrow < len(matrix[0]) and 0 <= ncol < len(matrix) and matrix[nrow][ncol] == matrix[row][col] + 1:
                    stack.append((nrow, ncol))
        
    return len(set(reachable_9s)), len(reachable_9s)

p1, p2 = 0, 0
total = 0
for i, line in enumerate(M):
    for j, num in enumerate(line):
        if num == 0:
            result = dfs(M,(i, j))
            p1 += result[0]
            p2 += result[1] 


print(f"{p1=}\n{p2=}")