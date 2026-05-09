function solution(arr) {
    return arr.reduce((sum, x) => sum+x, 0) / arr.length;
}