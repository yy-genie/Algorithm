# 큐의 크기
N = 10
# 공백 큐 생성
q = [0] * N
front = rear = -1
# front : 삭제된 원소의 위치
# rear : 마지막 원소의 위치

for i in range(1, 11):
    # 삽입 할 때는 rear+1 자리
    rear += 1
    q[rear] = i
print(q)
print(front, rear)

for i in range(10):
    # 삭제할때는 front+1 자리
    front += 1
    # print(q[front], end = "")
print(q)
print(front, rear)