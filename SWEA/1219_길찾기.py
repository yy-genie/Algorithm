T = 10
for tc in range(1, T+1):
    N, E = map(int, input().split())
    path = list(map(int, input().split()))
    graph = {}

    for n in range(E):
        # 그래프 입력
        depart, arrive = path[n*2], path[n*2+1]
        if depart not in graph.keys():
            graph[depart] = []
        graph[depart].append(arrive)

    visited = [False] * (100)
    # S : 출발 노드, G : 도착 노드
    S, G = 0, 99
    stack = [S]
    visited[S] = True
    answer = 0

    while stack:
        node = stack.pop()

        if node == G:
            answer = 1
            break
        if node in graph: 
            for n in graph[node]:
                if visited[n] == False:
                    visited[n] = True
                    stack.append(n)

    print(f'#{tc} {answer}')