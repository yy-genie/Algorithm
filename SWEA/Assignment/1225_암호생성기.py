T = 10
for tc in range(1, T+1):
    t = input()
    arr = list(map(int, input().split()))
    N = len(arr)

    q = [0] * (8)
    rear = front = -1

    # arr의 원소를 맨 앞부터 차례대로 q에 삽입
    for i in arr:
        rear = (rear + 1) % N
        q[rear] = i

    # q의 맨 앞에서 원소를 꺼내서 다시 맨 뒤로 삽입
    front += 1
    d = 1
    while q[front] > 0:
        if d > 5:
            d = 1
        q[front] -= d
        if q[front] <= 0:
            q[front] = 0
            front = (front+1) % N
            rear = (rear+1) % N
            break
        front = (front+1) % N
        rear = (rear+1) % N
        d += 1
    answer = q[front:] + q[:rear+1]
    print(f'#{tc}',*answer)