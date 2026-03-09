T = int(input())
D = [(0, 1), (1, 0)]

def path(i, j, total):
    global answer

    if total >= answer:
        return

    if i == N-1 and j == N-1:
        answer = total
        return
    
    for dx, dy in D:
        ni = i+dx
        nj = j+dy
        if 0<=ni<N and 0<=nj<N:
            path(ni, nj, total+arr[ni][nj])


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = arr[0][0]
    answer = float('inf')

    path(0, 0, total)

    print(f'#{tc} {answer}')