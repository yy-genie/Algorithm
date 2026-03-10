T = int(input())

def comb(cnt, selected, start):
    global answer
    # 원소의 개수가 N개
    if cnt == N:
        # N개 원소의 합이 K일 때
        if sum(selected) == K:
            answer += 1
        return

    for i in range(start, 12):
        comb(cnt+1, selected + [A[i]], i+1)

for tc in range(1, T+1):
    # 원소 개수 N개, 합이 K
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]
    answer = 0

    comb(0, [], 0)

    print(f'#{tc} {answer}')