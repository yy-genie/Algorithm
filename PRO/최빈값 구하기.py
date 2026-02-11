def solution(array):
    count = [0] * (max(array)+1)
    for i in array:
        count[i] += 1
    
    answer = count.index(max(count))

    value = max(count)
    count.pop(count.index(max(count)))
    for i in count:
        if i == value:
            answer = -1

    return answer


# Test
print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))
