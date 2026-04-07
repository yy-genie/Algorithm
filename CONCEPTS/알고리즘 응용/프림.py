"""
입력
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""

# 힙에 가중치를 기준으로 원소를 삽입 or 제거
# 원소를 제거 => 가중치가 가장 작은 원소가 뿅
from heapq import heappop, heappush

# V : 정점의 개수, E : 간선의 개수
V, E = map(int, input().split())

# 인접리스트
G = [[] for _ in range(V)]

for i in range(E):
    # s에서 e로 가는 간선의 가중치 w
    s, e, w = map(int, input().split())
    G[s].append((e, w))
    G[e].append((s, w))

'''
[PRIM 알고리즘]
1. 임의의 정점을 하나 골라서 시작
2. 내가 지금까지 골랐던 정점들과 인접하는 정점중에 최소 가중치를 가진 간선을 선택(조건 : 이전에 선택한 적 없고 정점과 이어진 간선) -> 최소힙 사용
3. MST가 만들어질 때까지 반복
'''

def prim(start):
    # 우선순위큐(최소합)
    heap = []
    # 중복체크배열 (visited 느낌)
    MST = [0] * V
    # 최소 비용
    min_w = 0
    # 정점을 선택한 횟수
    v_cnt = 0

    # 힙에 시작 정점 추가 (시작정점 추가할땐 가중치 0)
    heappush(heap, (0, start))

    # 가중치가 최소인 간선을 선택
    while v_cnt < V and heap:
        # w : 가중치 => 최소힙이니 최소 가중치 반환, v : 최소가중치를 가진 간선의 도착지점
        w, v = heappop(heap)

        if MST[v]:
            # 이미 포함되어 있으면 다음 최소 가중치 간선 꺼내기 위해 continue
            continue

        # MST에 v 포함
        MST[v] = 1
        # 가중치 합 계산
        min_w += w
        # 선택횟수 +1
        v_cnt += 1
        
        # v를 MST에 포함했으니 v에서 갈 수 있는 정점도 힙에 추가
        for nv, nw in G[v]:
            # nv : v에서 갈 수 있는 정점 번호, nw : 그때 간선의 가중치
            
            if MST[nv]:
                continue
            
            heappush(heap, (nw, nv))

    return min_w

print(f'MST 가중치 : {prim(0)}')
print(f'MST 가중치 : {prim(4)}')