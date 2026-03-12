T = int(input())
for tc in range(1, T+1):
    N, CAL = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (N+1)
    total_cal = 0

    for i in range(1, N+1):
        if total_cal < CAL:
            dp[i] = dp[i-1] + arr[i][0]
            total_cal += arr[i][1]
        else:
            continue

    answer = 0

    print(f'#{tc} {answer}')



# 아직 못 푼 거임