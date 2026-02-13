T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = [0] * (N+M+100)
    rear = front = -1

    # arr의 원소를 맨 앞부터 차례대로 q에 삽입
    for i in arr:
        rear = (rear + 1) % N
        q[rear] = i

    # q의 맨 앞에서 원소를 꺼내서 다시 맨 뒤로 삽입 M번
    for i in range(M):
        front = (front+1) % N
        rear = (rear+1) % N

    # q의 맨 앞에 있는 원소를 출력
    print(f'{tc} {q[front+1]}')