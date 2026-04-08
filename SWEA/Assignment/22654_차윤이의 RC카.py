T = int(input())    
def rc(command,n_y,n_x):
    pos = 0 
    for j in command:
        if j == 'A'or j=='Y':
        
            n_y += dr[pos]
            n_x += dc[pos]
            if 0 > n_y or 0 > n_x or N <= n_y or N <= n_x :
                n_y -= dr[pos]
                n_x -= dc[pos]
                continue
            
            if arr[n_y][n_x] =='T':
                n_y -= dr[pos]
                n_x -= dc[pos]
                continue

        if j == 'L':
            pos = abs((pos+1) % 4)
            
        if j == 'R':
            pos = abs((pos+3) % 4)
    if arr[n_y][n_x] =='Y':
        return '1 '
    
    else: return '0 '
# 상 우 하 좌 
dr = [-1,0,1,0]
dc = [0,-1,0,1]

for tc in range(1,T+1):
    N = int(input())

    arr = [list(input().strip())for _ in range(N)]

    Q = int(input())

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                s_y = i
                s_x = j
    answer = ''

    for i in range(Q):
        move, command = list(input().split())

        answer += (rc(command,s_y,s_x))

    print(f'#{tc} {answer}')