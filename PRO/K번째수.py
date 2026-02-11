def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0]
        end = i[1]
        num = i[2]
        new_array = array[start-1:end]
        new_array.sort()
        # print(new_array)
        if len(new_array) >= 3:
            answer.append(new_array[num-1])
        else:
            answer.append(new_array[-1])
    return answer

# Test
# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))