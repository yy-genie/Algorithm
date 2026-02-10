T = int(input())
for tc in range(1, T+1):
    # V : 노드 개수, E : 간선 개수
    V, E = map(int, input().split())
    graph = {}

    for _ in range(E):
        # 그래프 입력
        depart, arrive = map(int, input().split())
        if depart not in graph.keys():
            graph[depart] = []
        graph[depart].append(arrive)

    visited = [False] * (V+1)
    # S : 출발 노드, G : 도착 노드
    S, G = map(int, input().split())

    stack = [S]
    visited[S] = True
    answer = 0

    while stack:
        node = stack.pop()

        if node == G:
            answer = 1
            break
        if node in graph:  # ex. 1 : [4, 3]
            for n in graph[node]:
                if visited[n] == False:
                    visited[n] = True
                    stack.append(n)

    print(f'#{tc} {answer}')