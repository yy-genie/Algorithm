T = int(input())

D = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(N):
            cnt = 0
            cnt_1 = arr[i][j]
            cnt_2 = arr[i][j]
            for d in D[::2]:
                for c in range(1, M):
                    ni = i+d[0]*c
                    nj = j+d[1]*c
                    if 0<=ni<N and 0<=nj<N:
                        cnt_1 += arr[ni][nj]
            for d in D[1::2]:
                for c in range(1, M):
                    ni = i+d[0]*c
                    nj = j+d[1]*c
                    if 0<=ni<N and 0<=nj<N:
                        cnt_2 += arr[ni][nj]
            if cnt_1 > cnt_2:
                cnt = cnt_1
            else:
                cnt = cnt_2

            if cnt >= answer:
                answer = cnt

    print(f'#{tc} {answer}')