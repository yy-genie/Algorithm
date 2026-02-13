T = int(input())
def lst_sum(row, sum):
    global min_sum
    if row == N:
        if min_sum > sum:
            min_sum = sum
        return  
    if sum > min_sum:
        return

    num = matrix[0][0]
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            lst_sum(row + 1, sum + matrix[row][j])
            visited[j] = 0
         
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = 999999
    lst_sum(0, 0)
    print(f"#{tc} {min_sum}")