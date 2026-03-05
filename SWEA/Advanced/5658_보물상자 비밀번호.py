T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = list(input())

    # N//4개씩 리스트에 넣기
    lst = []
    for i in range(N//4):
        temp = num
        if i > 0:
            # 회전할때마다 배열 한칸씩 밀기
            temp = num[N-i::] + num[:N-i:]
        for j in range(0, N, N//4):
            lst.append(temp[j:j+N//4:1])

    # 10진수로 변환할 숫자들 담을 리스트
    result = []
    for j in range(N):
        # 내부 리스트의 원소들 한 문자열로 합친 후 10진수로 변환해 append
        result.append(int(''.join(lst[j]), 16))

    # 중복 숫자 제거
    result = list(set(result))
    # 내림차순 정렬
    result.sort(reverse=True)
    # K번째로 큰 수 출력
    print(f'#{tc} {result[K-1]}')