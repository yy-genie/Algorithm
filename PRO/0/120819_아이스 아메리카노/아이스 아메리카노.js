function solution(money) {
    var answer = [];
    var cnt = 0
    while (money >= 5500) {
        cnt += 1
        money -= 5500
    }
    answer.push(cnt)
    answer.push(money)
    return answer;
}