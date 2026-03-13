T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
     
    max_prob = 0
    selected = [0] * N
 
    def backtracking(idx, prob):
        global max_prob
 
        if prob < max_prob:
            return
 
        if idx == N:
            max_prob = max(max_prob, prob)
 
        for j in range(N):
            if not selected[j] and matrix[idx][j] != 0:
                selected[j] = 1
                backtracking(idx + 1, prob * matrix[idx][j] / 100)
                selected[j] = 0
 
    backtracking(0, 100)
    print(f"#{tc} {max_prob:.6f}")