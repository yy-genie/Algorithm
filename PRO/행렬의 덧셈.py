def solution(arr1, arr2):
    answer = arr1
    N = len(arr1)
    M = len(arr1[0])
    for i in range(N):
        for j in range(M):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

# arr1 = [[1],[2]]
# arr2 = [[3],[4]]
# print(solution(arr1, arr2))