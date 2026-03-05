code_table = {
    "0001101": "0",
    "0011001": "1",
    "0010011": "2",
    "0111101": "3",
    "0100011": "4",
    "0110001": "5",
    "0101111": "6",
    "0111011": "7",
    "0110111": "8",
    "0001011": "9",
}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    code = [input() for _ in range(N)]

    # code 를 뒤에서부터 순회
    for i in range(N):
        for j in range(M - 1, 54, -1):
            if code[i][j] == "1":
                # 코드 의심 부분
                line = code[i][j - 55:j + 1]
                # 코드 검증
