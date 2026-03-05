T = int(input())
for tc in range(1, T+1):
    N = int(input())
    id_person = list(map(int, input().split()))

    answer = 0
    for i in id_person:
        answer ^= i

    print(f'#{tc} {answer}')