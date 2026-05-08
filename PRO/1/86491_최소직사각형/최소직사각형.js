function solution(sizes) {
    var answer = 0;
    var n = sizes.length
    var w = []
    var h = []
    
    for (s of sizes) {
        if (s[0] < s[1]) {
            w.push(s[1])
            h.push(s[0])
        } else {
            w.push(s[0])
            h.push(s[1])
        }
    }
    
    return Math.max(...w)*Math.max(...h);
}