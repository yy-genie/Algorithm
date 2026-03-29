from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, num):
    q = deque()
    q.append((x, y))
    board[x][y] = num

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                board[nx][ny] = num
                q.append((nx, ny))

island_num = 2

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            bfs(i, j, island_num)
            island_num += 1

edges = []

def make_bridge(x, y):
    for d in range(4):
        nx = x
        ny = y
        length = 0

        while True:
            nx += dx[d]
            ny += dy[d]

            if not (0 <= nx < N and 0 <= ny < M):
                break

            if board[nx][ny] == board[x][y]:
                break

            if board[nx][ny] == 0:
                length += 1
                continue

            if length >= 2:
                edges.append((length, board[x][y], board[nx][ny]))
            break

for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            make_bridge(i, j)

parent = [i for i in range(island_num)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

edges.sort()

result = 0
count = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += cost
        count += 1

# 모든 섬 연결 확인
root = find(2)
for i in range(3, island_num):
    if find(i) != root:
        print(-1)
        break
else:
    print(result)