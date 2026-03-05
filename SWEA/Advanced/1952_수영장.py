T = int(input())

for tc in range(1, T+1):
    price_d, price_m, price_3m, price_y = map(int, input().split())
    plan = list(map(int, input().split()))

    # month_cost[i] = i달에 산정한 최소 비용 
    month_cost = [0]  # 각 달이랑 인덱스 맞추기 위해 [0]에 0 넣어놓음
    # dp[i] = i달까지의 최소 비용
    dp = [0]*13  # 마찬가지로 인덱스 맞추려고 원소 13개

    # month_cost 채우기 (price_d*n일 vs price_m 중 작은값 append)
    for i in range(len(plan)):
        month_cost.append(min(plan[i]*price_d, price_m))

    # dp[i] 계산
    for i in range(1, 13):
        # 기본 dp[i] 계산
        dp[i] = dp[i-1] + month_cost[i]

        # 3월부턴 3달치 이용권도 고려해서 계산
        if i >= 3 and i < 12:
            dp[i] = min(dp[i], dp[i-3] + price_3m)

        # 12월일 경우 : (10, 11, 12) 3달치 이용권 사용도 가능하지만
        # dp[10] + (11, 12월) 3달치 이용권 and dp[11] + (12월) 3달치 이용권도 가능
        if i == 12:
            dp[i] = min(dp[i], dp[i-3] + price_3m, dp[i-2] + price_3m, dp[i-1] + price_3m)

    # 계산된 dp[12]와 1년 이용권 가격 비교
    answer = min(dp[12], price_y)

    print(f'#{tc} {answer}')



'''
input
이용권 가격 : 10 40 100 300 (각 1일, 1달, 3달, 1년)
이용 계획 : 0 0 2 9 1 5 0 0 0 0 0 0 (각 달의 이용 일자 수)

3달 짜리는 11, 12월에도 사용 가능
모든 이용권 1일부터 시작
가장 적은 비용으로 이용할 수 있는 방법
정답 : 최소 비용 출력

dp[i] = 1~i월까지 최소 비용
month_cost[i] = i월에서의 최소 비용 (1일 이용권 vs 1달 이용권)
'''