T = int(input())

def path(now_room, e):
    global answer

    # 가지치기
    if e >= answer:
        return 
    
    # 종료조건 : 모든 행 순찰 완료
    if False not in visited:
        e += arr[now_room][0]
        answer = min(e, answer)
        return 

    # 재귀호출 : 선택하지 않은 구역 중 하나 선택
    for next_room in range(N):
        if not visited[next_room]:
            visited[next_room] = True
            e_sum = arr[now_room][next_room]
            visited[next_room] = True
            path(next_room, e + e_sum)
            visited[next_room] = False


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = float('inf')
    visited = [False] * N
    visited[0] = True

    path(0, 0)

    print(f'#{tc} {answer}')