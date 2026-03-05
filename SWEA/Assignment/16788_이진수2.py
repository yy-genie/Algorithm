T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ''

    for _ in range(12):
        N *= 2
        if N >= 1:
            ans += '1'
            N -= 1
        else:
            ans += '0'
        if N == 0:
            break
    else:
        ans = 'overflow'
    
    print(f'#{tc} {ans}')