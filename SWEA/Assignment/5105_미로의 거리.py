T = int(input())
D = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs_maze(si, sj):
    q = [(si, sj)]
    visited = [[-1]*N for _ in range(N)]
    visited[si][sj] = 0
    
    while q:
        i, j = q.pop(0)

        for d in D:
            ni = i+d[0]
            nj = j+d[1]
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] != 1 and visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i][j]+1
                    q.append((ni, nj))

                    if arr[ni][nj] == 3:
                        return visited[ni][nj]-1
    return 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                answer = bfs_maze(i, j)

    print(f'#{tc} {answer}')