T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[False]*N for _ in range(N)]
    D = [(-1, 0), (-1, 1), (-1, -1)]
    answer = 0

    def backtrack(row):
        global answer

        # 종료 조건
        if row == N:
            answer += 1
            return

        for col in range(N):
            # 행, 열, 대각선 검사
            check = True
            if row > 0:
                for dx, dy in D:
                    for r in range(1, row+1):
                        ni = row + r*dx
                        nj = col + r*dy
                        if 0<=ni<N and 0<=nj<N:
                            if visited[ni][nj]:
                                check = False
                                break
                    if not check:
                        break

            # 열 선택
            if check:
                visited[row][col] = True
                backtrack(row+1)
                visited[row][col] = False
            
    backtrack(0)

    print(f'#{tc} {answer}')