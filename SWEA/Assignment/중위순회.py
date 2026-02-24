T = int(input())

def inorder(node):
    inorder(left[node])
    answer.append(c[node])
    inorder(right[node])

for tc in range(1, T+1):
    N = int(input())
    left = []
    right = []
    c = []
    answer = []
    for _ in range(1, N+1):
        temp = list(input().split())
        node = temp[0]
        c[node] = temp[1]
        if len(temp) >= 3:
            left[node] = int(temp[2])
        if len(temp) == 4:
            right[node] = int(temp[3])

    inorder(1)
    print(f'#{tc} {answer}')