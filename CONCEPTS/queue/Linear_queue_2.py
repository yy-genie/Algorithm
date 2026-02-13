N = 200000

# 파이썬의 리스트 메서드로 구현
q = []

# 원소 10개 추가
for i in range(1, 11):
    q.append(i)
print(q)

# 원소 10개 삭제
for i in range(10):
    e = q.pop(0)
print(q)

# 큐 구현
q2 = [0] * N
front = rear = -1

for i in range(N):
    rear += 1
    q2[rear] = i
print(q2, front, rear)

for i in range(N):
    front += 1
print(q2, front, rear)