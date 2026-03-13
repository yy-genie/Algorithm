T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    wires = []
    answer = 0

    for _ in range(N):
        start, end = map(int, input().split())

        for prev_start, prev_end in wires:
            if start > prev_start and end < prev_end:
                answer += 1

            if start < prev_start and end > prev_end:
                answer += 1

        wires.append((start, end))

    print(f'#{tc} {answer}')