T = int(input())
# 교환횟수k 를 단계로
def solve(k):
    global max_price

    # 가지치기
    if (k, ''.join(numbers)) in check:
        return

    check.add((k, ''.join(numbers)))
    
    # 종료
    if k == cnt:
        result = int(''.join(numbers))
        max_price = max(max_price, result)
        return

    # 재귀
    for i in range(N-1):
        for j in range(i+1, N):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            solve(k+1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


for tc in range(1, T + 1):
    numbers, cnt = input().split()
    cnt = int(cnt)
    numbers = list(numbers)

    N = len(numbers)
    max_price = 0
    check = set()

    solve(0)

    print(f"#{tc} {max_price}")