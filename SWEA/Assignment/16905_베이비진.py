T = int(input())

def babyjin(p1, p2):
    for i in range(10):
        if p1[i] == 3:
            return 1
        if p2[i] == 3:
            return 2

    for j in range(8):
        if p1[j] >= 1:
            if p1[j+1] >= 1 and p1[j+2] >= 1:
                return 1
        if p2[j] >= 1:
            if p2[j+1] >= 1 and p2[j+2] >= 1:
                return 2
    return 0

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    player1 = [0]*10
    player2 = [0]*10

    for i in range(len(arr)):
        if i % 2 == 0:
            player1[arr[i]] += 1
        else:
            player2[arr[i]] += 1
        if i>=5:
            winner = babyjin(player1, player2)

    # print(player1, player2)

    print(f'#{tc} {winner}')