T = int(input())

def binary_search(start, end, mid, target, check):
    global answer

    if start > end:
        return
    
    # 종료 조건 : m 찾는 경우
    if A[mid] == target:
        answer += 1
        return

    # target < mid
    if A[mid] > target:
        if check == -1:
            return
        binary_search(start, mid-1, (start+mid-1)//2, target, -1)
    
    # target > mid
    if A[mid] < target:
        if check == 1:
            return
        binary_search(mid+1, end, (mid+1+end)//2, target, 1)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    answer = 0

    for i in range(M):
        binary_search(0, N-1, (N-1)//2, B[i], 0)

    print(f'#{tc} {answer}')