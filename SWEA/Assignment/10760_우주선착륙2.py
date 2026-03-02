T = int(input())

D = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            cnt = 0
            for d in D:
                ni = i+d[0]
                nj = j+d[1]
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] < arr[i][j]:
                    cnt += 1
            if cnt >= 4:
                answer += 1

    print(f'#{tc} {answer}')