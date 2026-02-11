def solution(citations):
    n = len(citations)
    h = []
    citations.sort()
    for i in range(n+1):
        cnt = 0
        for j in range(n):
            if citations[j] >= i:
                cnt += 1
        if cnt >= i:
            h.append(i)
    return max(h)

# arr = [5, 5, 5, 5, 5]
# print(solution(arr))