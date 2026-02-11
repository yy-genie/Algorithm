def solution(nums):
    N = len(nums)//2
    nums = list(set(nums))

    if len(nums) >= N:
        return N
    else:
        return len(nums)

# lst = [3, 1, 2, 3]
# print(solution(lst))