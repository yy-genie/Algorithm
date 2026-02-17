'''
1. 이동 방향은 정해진 순서로 4가지 (1, 1), (1, -1), (-1, -1), (-1, 1)
2. 사각형 만들기 - 시작점에서 a칸, b칸, a칸, b칸
3. 중복 디저트 금지 (같은 숫자 안됨)

해야할 것 : 시작점(i, j), 변 길이(a, b) 정하기
'''

T = int(input())

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    answer = -1

    # 시작점(i, j)
    for i in range(N):
        for j in range(N):
            # a 길이
            for a in range(1, N+1):
                # b 길이
                for b in range(1, N+1):
                    # 디저트 리스트
                    dessert = []
                    # 현재 위치
                    ni, nj = i, j
                    valid = True

                    # 4방향 이동
                    for d in range(4):  # d = 0, 1, 2, 3
                        if d % 2 == 0:
                            steps = a
                        else:
                            steps = b
                        
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
                            dessert.append(arr[ni][nj])
                        if not valid:
                            break
                    
                    # 시작점으로 돌아왔는지 확인
                    if valid and ni == i and nj == j:
                        # 기존 answer와 현재 루트 디저트 개수 비교
                        answer = max(answer, len(dessert))

    print(f"#{tc} {answer}")