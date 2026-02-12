T = int(input())

# ↘ ↙ ↖ ↗
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    answer = -1

    def dfs(si, sj, i, j, direction, dessert_set):
        global answer
        
        for d in range(direction, 4):  # 현재 방향 또는 다음 방향만 가능
            ni = i + di[d]
            nj = j + dj[d]
            
            if 0 <= ni < N and 0 <= nj < N:
                
                # 출발점으로 돌아왔고 4방향 다 썼다면 성공
                if ni == si and nj == sj and d == 3:
                    answer = max(answer, len(dessert_set))
                    return
                
                # 아직 안 먹은 디저트라면
                if arr[ni][nj] not in dessert_set:
                    dfs(si, sj, ni, nj, d, dessert_set | {arr[ni][nj]})

    for i in range(N):
        for j in range(N):
            dfs(i, j, i, j, 0, {arr[i][j]})

    print(f"#{tc} {answer}")