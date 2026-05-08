function solution(players, callings) {
    var map = new Map()
    players.forEach((name, idx) => {
        map.set(name, idx)
    })
    
    for (c of callings) {
        i = map.get(c)
        temp = players[i-1]
        
        players[i-1] = players[i]
        players[i] = temp
        
        map.set(c, i-1)
        map.set(temp, i)
    }
    
    return players;
}