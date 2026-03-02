N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

visited = [[False] * N for _ in range(N)]
home_lst = []

for i in range(N):
    for j in range(N):
        # 집이 있고 and 아직 방문 X
        if arr[i][j] == 1 and not visited[i][j]:
            stack = [(i, j)]
            visited[i][j] = True
            home = 1
            # DFS로 연결된 집 전부 탐색
            while stack:
                x, y = stack.pop()
                # 방향 지정
                for dx, dy in D:
                    nx = x + dx
                    ny = y + dy
                    # 범위 체크
                    if 0 <= nx < N and 0 <= ny < N:
                        # 집이 존재 and 아직 방문 X
                        if arr[nx][ny] == 1 and not visited[nx][ny]:
                            # 방문 처리
                            visited[nx][ny] = True
                            # 같은 단지이므로 스택에 추가
                            stack.append((nx, ny))
                            home += 1

            home_lst.append(home)

home_lst.sort()
print(len(home_lst))
for h in home_lst:
    print(h)