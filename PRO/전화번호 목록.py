# 완전탐색 -> 효율성 테스트에서 시간 초과
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        number = phone_book[i]
        for j in range(len(phone_book)):
            if i == j:
                continue
            if phone_book[j][:len(number)] == number:
                answer = False
                return answer
    return answer

# Test
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))