T = int(input())

for tc in range(1, T + 1):
    # 제품의 종류 N개 / 공장 개수 N개
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # matrix[i][j] : i번 제품을 j번 공장에서 생산시 비용

    # 문제에서 원하는 답 : 모든 제품을 생산하는데 드는 최소 비용
    min_cost = float("inf")


    # idx : 현재 제품 번호
    # selected : 이전에 제품을 생산한적 있는 공장 번호 리스트,
    # [1,2] => 1번, 2번공장은 이전에 다른 제품을 생산 하기로 했음,
    # cost : idx번 제품까지 생산하는데 드는 비용
    def backtracking(idx, selected, cost):
        global min_cost

        # 0. 가지치기
        if cost >= min_cost:
            return

        # 1. 종료조건
        if idx == N:
            # 지금까지 계산한 생산 비용 cost 와
            # 이전 최소 생산비용 min_cost 중에 작은것 선택
            min_cost = min(cost, min_cost)
            return

        # 2. 재귀호출
        # idx번 제품을 몇번 공장에서 생산할건지
        # 공장번호를 j 라고 하면
        for j in range(N):
            # j번 공장은 이전에 다른 제품을 생산한적이 없어야 한다.
            # selected를 통해 체크
            # j번공장이 이전에 다른 제품을 생산한적없다면 idx번 제품을 생산하기로 하고
            # idx+1 번 제품을 누가 생산할건지 정하러 재귀호출
            if j not in selected:
                # idx번 제품을 j번 공장이 생성
                backtracking(idx + 1, selected + [j], cost + matrix[idx][j])


    backtracking(0, [], 0)

    print(f"#{tc} {min_cost}")
