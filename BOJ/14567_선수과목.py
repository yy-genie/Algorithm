N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
semester = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        semester[i] = 1

while queue:
    now = queue.popleft()
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            semester[nxt] = semester[now] + 1
            queue.append(nxt)

print(*semester[1:])