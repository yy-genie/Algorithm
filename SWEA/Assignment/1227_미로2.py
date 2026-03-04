D = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def maze_dfs(si, sj):
    q = [(si, sj)]
    visited = [[False]*N for _ in range(N)]
    visited[si][sj] = True

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

for tc in range(1, 11):
    t = int(input())
    N = 100
    arr = [list(map(int, input())) for _ in range(N)]
    
    answer = maze_dfs(1, 1)

    print(f'#{tc} {answer}')