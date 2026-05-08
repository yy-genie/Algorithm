function solution(numbers) {
    var answer = -1;
    var arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = arr.filter(x => !numbers.includes(x))
    answer = arr.reduce((sum, x) => sum+x, 0)
    return answer;
}