T = int(input())

# 전치행렬 구현
def matrix_T(arr):
    new_arr = [[0]*(len(arr)) for _ in range(len(arr[0]))]
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            new_arr[i][j] = arr[j][i]
    return new_arr

# 한 줄씩 경사로 가능/불가능 여부 체크
def check(path):
    # 경사로 설치 여부 표시할 visited 배열
    visited = [False]*N
    
    for i in range(N-1):
        # 높이 같을 때 다음 인덱스로
        if path[i] == path[i+1]:
            continue

        # 높이 차이 1 초과면 불가능
        if abs(path[i] - path[i+1]) > 1:
            return 0
        
        # 내리막 경사로
        if path[i]-1 == path[i+1]:
            h = path[i+1]
            # i+1 부터 X칸 확인
            if i+X >= N:  # 인덱스 범위 확인
                return 0
            for j in range(i+1, i+X+1):  # i+1부터 i+X까지
                if path[j] != h or visited[j]:
                    return 0
            # 경사로 설치 표시
            for j in range(i+1, i+X+1):
                visited[j] = True

        # 오르막 경사로
        elif path[i]+1 == path[i+1]:
            h = path[i]
            # i부터 왼쪽으로 X칸 확인
            if i-X+1 < 0:
                return 0
            for j in range(i, i-X, -1):
                if path[j] != h or visited[j]:
                    return 0
            # 경사로 설치 표시
            for j in range(i, i-X, -1):
                visited[j] = True

    return 1

for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    # 테케 line 한 줄씩 검사
    for path in arr:
        # 해당 줄이 가능할 경우 1리턴 받아서 누적합
        total += check(path)

    # 세로의 경우 전치행렬 활용
    arr2 = matrix_T(arr)
    # 가로와 동일 방식
    for path in arr2:
        total += check(path)

    print(f'#{tc} {total}')