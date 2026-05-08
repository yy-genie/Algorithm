function solution(n) {
    var answer = 0;
    var x = 1
    var temp = 0
    
    while (!temp) {
        if (n%x === 1) {
            temp = 1
        }
        x += 1
    }
    return x-1;
}