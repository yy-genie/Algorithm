T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = list(input())

    lst = []
    for i in range(N//4):
        temp = num
        if i > 0:
            temp = num[N-i::] + num[:N-i:]
        for j in range(0, N, N//4):
            lst.append(temp[j:j+N//4:1])

    result = []
    for j in range(N):
        result.append(int(''.join(lst[j]), 16))
    result = list(set(result))
    result.sort(reverse=True)

    print(f'#{tc} {result[K-1]}')