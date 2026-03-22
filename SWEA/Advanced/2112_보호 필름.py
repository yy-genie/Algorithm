T = int(input())

# K 만족하는지 확인
def check():
    for j in range(W):
        cnt = 1  # 연속 특성 개수
        max_cnt = 1  # 가장 긴 cnt
        for i in range(1, D):
            # 현재 특성과 이전 행 특성이 같으면
            if arr[i][j] == arr[i-1][j]:
                cnt += 1
            # 다를 경우 cnt 초기화
            else:
                cnt = 1
            # max_cnt 업뎃
            if cnt > max_cnt:
                max_cnt = cnt
        # 한 열이라도 연속 성분이 K개보다 작으면 실패
        if max_cnt < K:
            return False
    # 모두 통과할 경우 성공
    return True

# dfs 완탐
# idx : 현재 행, cnt : 약품 투여 횟수
def dfs(idx, cnt):
    global answer

    # 현재 약물 투입 횟수가 answer보다 크면 가지치기
    if cnt >= answer:
        return

    # 종료조건 (idx 마지막 행까지 확인)
    if idx == D:
        # 성공 여부 체크
        if check():
            # 성공이라면 answer 최소로 갱신
            answer = min(answer, cnt)
        return
    
    # case1 : 약품 투입 X
    # 아무것도 안바르고 idx+1
    dfs(idx+1, cnt)
    # case2,3 들어가기 전 원본 배열 저장
    original_row = arr[idx][::]

    # case2 : A 투입
    # idx번 행 전체를 0으로
    arr[idx] = [0]*W
    dfs(idx+1, cnt+1)

    # case3 : B 투입
    # idx번 행 전체를 1로
    arr[idx] = [1]*W
    dfs(idx+1, cnt+1)

    # case3까지 끝나면 복구
    arr[idx] = original_row

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]

    # K가 1인 경우는 무조건 답이 0
    if K == 1:
        print(f'#{tc} 0')
        continue

    # 최악의 경우는 K만큼 약품 투입
    answer = K
    dfs(0, 0)

    print(f'#{tc} {answer}')