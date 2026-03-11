T = int(input())

# 병합 정렬 함수
# 정렬할 범위를 인덱스로 지정
def merge_sort(start, end):
    # 1. 종료 조건 : 원소가 하나 남았을 때 (더 이상 분할 X)
    if start == end - 1:
        return start, end
    
    # 2. 재귀 호출 : 두 부분으로 나누고, 합칠 때 정렬
    mid = (start + end) // 2

    # 오른쪽, 왼쪽부분 다시 분할 후 정렬
    left_s, left_e = merge_sort(start, mid)
    right_s, right_e = merge_sort(mid, end)

    # 합치기
    merge(left_s, left_e, right_s, right_e)

    return start, end

# 주어진 왼쪽 부분과 오른쪽 부분을 합치는 함수
def merge(left_s, left_e, right_s, right_e):
    global cnt

    l, r = left_s, right_s
    # 왼쪽 부분 + 오른쪽 부분 길이
    N = right_e - left_s
    result = [0] * N

    # result 배열에 들어갈 원소의 다음 자리
    idx = 0

    if arr[left_e - 1] > arr[right_e - 1]:
            cnt += 1

    # 병합 시작 : 둘 중에 작은거 선택해서 result의 idx 위치에 넣기
    # 왼쪽 부분이나 오른쪽 부분이 둘 다 남아 있는 경우
    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            # 왼쪽 부분 젤 앞이 최소값
            result[idx] = arr[l]
            l += 1
            idx += 1
        else:
            result[idx] = arr[r]
            r += 1
            idx += 1

    # 오른쪽 부분만 남아있을때
    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1

    # 왼쪽 부분만 남아있을때
    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    for i in range(N):
        arr[left_s + i] = result[i]


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    merge_sort(0, N)

    print(f'#{tc} {arr[N//2]} {cnt}')