T = int(input())

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            c = arr[i][j]
            for d in D:
                for x in range(1, c+1):
                    ni = i+d[0]*x
                    nj = j+d[1]*x
                    if 0<=ni<N and 0<=nj<M:
                        cnt += arr[ni][nj]
            if cnt > answer:
                answer = cnt

    print(f'#{tc} {answer}')