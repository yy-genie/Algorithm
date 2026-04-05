def solution(tickets):
    graph = {}
    
    # 그래프
    for a, b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    
    # 사전순 정렬
    for key in graph:
        graph[key].sort()
    
    path = ["ICN"]
    
    def dfs(airport):
        # 모든 티켓 사용
        if len(path) == len(tickets) + 1:
            return True
        
        if airport not in graph:
            return False
        
        for i in range(len(graph[airport])):
            next_airport = graph[airport][i]
            
            if next_airport != "":
                graph[airport][i] = ""  # 사용 처리
                path.append(next_airport)
                
                if dfs(next_airport):
                    return True
                
                # 백트래킹
                path.pop()
                graph[airport][i] = next_airport
        
        return False
    
    dfs("ICN")
    
    return path