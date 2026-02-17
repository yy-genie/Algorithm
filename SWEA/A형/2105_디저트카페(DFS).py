T = int(input())

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # dfs 어케해요 ㅠㅠ

    print(f"#{tc} {answer}")