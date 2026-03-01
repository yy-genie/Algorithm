T = int(input())

def cost(K):
    return K*K + (K-1)*(K-1)

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    # 배열 좌표 x, y
    for x in range(N):
        for y in range(N):
            # 서비스 영역 크기 k
            for k in range(1, 2*N):  # k : 1 2 3 ...
                home = 0
                # 마름모 순회 (GPT 도움!!)
                # ----------------------------------------
                K = k - 1
                # 위 K줄 ~ 아래 K줄 (몇 줄 볼지 결정)
                for dx in range(-K, K+1):
                    # 해당 줄에서 좌우 범위 계산
                    limit = K - abs(dx)
                    # 그 줄의 모든 칸 방문
                    for dy in range(-limit, limit+1):
                        ni = x + dx
                        nj = y + dy
                # ----------------------------------------
                        # 범위 확인
                        if 0<=ni<N and 0<=nj<N:
                            # 집이 있을 경우
                            if arr[ni][nj] == 1:
                                home += 1
                # 이익 계산
                profit = M * home - cost(k)
                # 손해 여부
                if profit >= 0:
                    # home 개수 비교
                    if home > answer:
                        answer = home

    print(f'#{tc} {answer}')