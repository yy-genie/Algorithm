T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    
    if B < 2 or C < 3:
        answer = -1
    
    eat_count = 0

    # B 상자
    if B >= C:
        eat_count += B - (C - 1)
        B = C - 1

    # A 상자
    if A >= B:
        eat_count += A - (B - 1)
        A = B - 1

    if answer != -1:
        answer = eat_count

    print(f'#{tc} {answer}')