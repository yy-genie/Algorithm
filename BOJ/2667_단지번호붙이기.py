N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * N for _ in range(N)]

home_lst = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            stack = [(i, j)]
            visited[i][j] = True
            home = 1

            while stack:
                x, y = stack.pop()
                for dx, dy in D:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                            home += 1
            home_lst.append(home)
home_lst.sort()

print(len(home_lst))
for h in home_lst:
    print(h)