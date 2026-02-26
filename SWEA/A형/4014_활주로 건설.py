T = int(input())

def matrix_T(arr):
    new_arr = [[0]*(len(arr)) for _ in range(len(arr[0]))]
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            new_arr[i][j] = arr[j][i]
    return new_arr

def check(path):
    rtemp = path[0]
    ltemp = path[0]
    result = False
    answer = 0
    for j in range(1, N-X+1):
        if path[j] == rtemp:
            continue
        elif path[j] == rtemp-1:
            # 오른쪽으로 길이 X만큼 있는지 확인
            for d in range(X):
                if path[j+d] == rtemp-1:
                    result = True
                    continue
                else:
                    result = False
                    break
            if result:
                answer += 1
                rtemp = path[j]
        elif path[j]-1 == ltemp:
            # 왼쪽부터 길이 X만큼 있는지 확인
            cnt = 0
            for d in range(j+1):
                if path[d] == path[j]-1:
                    cnt += 1
                    result = True
                else:
                    result = False
                    break
            if cnt >= X:
                answer += 1
                ltemp = path[j]
        else:
            continue
    return answer
    
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    for path in arr:
        total += check(path)

    arr2 = matrix_T(arr)
    for path in arr2:
        total += check(path)

    print(f'#{tc} {total}')