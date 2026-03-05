'''
정수 N, M이 주어질 때, M의 이진수 표현의 마지막 
N 비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{tc} {"ON" if M & ((1<<N)-1) == (1<<N)-1 else "OFF"}')


'''
M = 29
16 8 4 1
11101

N = 3
(1<<3)-1 = 111

11101 & 00111 = 101

= M의 마지막 N 비트
'''