T = int(input())

# ↘ ↙ ↖ ↗
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    answer = -1

    # 1️⃣ 시작점
    for i in range(N):
        for j in range(N):

            # 2️⃣ 첫 번째 변 길이 a
            for a in range(1, N):

                # 3️⃣ 두 번째 변 길이 b
                for b in range(1, N):

                    dessert = set()
                    ni, nj = i, j
                    valid = True

                    # 4방향 이동
                    for d in range(4):
                        steps = a if d % 2 == 0 else b
                        
                        for _ in range(steps):
                            ni += di[d]
                            nj += dj[d]

                            # 범위 벗어나면 실패
                            if not (0 <= ni < N and 0 <= nj < N):
                                valid = False
                                break

                            # 중복 디저트면 실패
                            if arr[ni][nj] in dessert:
                                valid = False
                                break

                            dessert.add(arr[ni][nj])

                        if not valid:
                            break

                    # 시작점으로 돌아왔는지 확인
                    if valid and ni == i and nj == j:
                        answer = max(answer, len(dessert))

    print(f"#{tc} {answer}")