def solution(arr1, arr2):
    # arr2 전치행렬
    arr2 = matrix_T(arr2)
    N = len(arr1)
    M = len(arr2)
    # 연산 결과 넣을 answer 리스트 생성
    answer = [[0]*M for _ in range(N)]
    # answer[x][y]에 원소 넣기
    for x in range(N):
        e1 = arr1[x]
        for y in range(M):
            e2 = arr2[y]
            element = 0
            # 곱 연산
            for z in range(len(arr1[0])):
                element += e1[z] * e2[z]
            answer[x][y] = element
    return answer

# 전치행렬 함수 구현
def matrix_T(arr):
    new_arr = [[0]*(len(arr)) for _ in range(len(arr[0]))]
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            new_arr[i][j] = arr[j][i]
    return new_arr

# # Test
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))