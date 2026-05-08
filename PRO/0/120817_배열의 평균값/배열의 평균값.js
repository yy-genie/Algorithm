function solution(numbers) {
    var answer = 0;
    for (var x of numbers) {
        answer += x;
    }
    answer = answer/numbers.length
    return answer;
}