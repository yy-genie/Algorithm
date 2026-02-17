T = int(input())

# 출발점 찾기
def start_spot(arr, N):
    max_num = max(map(max, arr))
    spot = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_num:
                spot.append((i, j))
    return spot

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def find(i, j, length, cut_used):
    global answer
    answer = max(answer, length)

    # 방향 설정
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        # 범위 만족 & 방문 안했으면
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            # 봉우리 높이 비교
            if arr[ni][nj] < arr[i][j]:
                visited[ni][nj] = True
                find(ni, nj, length + 1, cut_used)
                visited[ni][nj] = False
            # 높이 때문에 못내려감, but 안깎음
            elif cut_used == 0:
                # 최대 K까지 깎기
                for k in range(1, K + 1):
                    if arr[ni][nj] - k < arr[i][j]:
                        temp = arr[ni][nj]
                        arr[ni][nj] = temp - k

                        visited[ni][nj] = True
                        find(ni, nj, length + 1, 1)
                        visited[ni][nj] = False
                        arr[ni][nj] = temp
                        break

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    starts = start_spot(arr, N)

    answer = 0
    visited = [[False]*N for _ in range(N)]

    for si, sj in starts:
        visited[si][sj] = True
        find(si, sj, 1, 0)
        visited[si][sj] = False

    print(f"#{tc} {answer}")