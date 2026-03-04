T = int(input())
D = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def maze_dfs(i, j):
    q = [(i, j)]
    visited = [[False]*N for _ in range(N)]
    visited[i][j] = True

    while q:
        i, j = q.pop(0)
        if arr[i][j] == 3:
            return 1
        for d in D:
            ni = i+d[0]
            nj = j+d[1]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] != 1 and not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = True
    return 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                answer = maze_dfs(i, j)

    print(f'#{tc} {answer}')