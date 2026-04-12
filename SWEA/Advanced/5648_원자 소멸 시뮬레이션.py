T = int(input())

D = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for tc in range(1, T + 1):
    N = int(input())
    atoms = []

    for _ in range(N):
        x, y, d, k = map(int, input().split())
        # 좌표를 2배로
        # 원자 간의 거리가 1일 때 마주보고 오면 0.5초 지점에서 충돌
        atoms.append([x * 2, y * 2, d, k])

    total = 0 

    # 최대 4000번
    for _ in range(4000):
        # 원자가 2개 미만
        if len(atoms) < 2:
            break

        # 원자 위치를 기록 딕셔너리 (Key: 좌표, Value: 원자 정보)
        hash_map = {}

        # 모든 원자 이동
        for x, y, d, k in atoms:
            nx = x + D[d][0]
            ny = y + D[d][1]

            # 이동한 좌표 기록
            if (nx, ny) not in hash_map:
                hash_map[(nx, ny)] = []
            hash_map[(nx, ny)].append((d, k))

        next_atoms = []

        # 이동 후 같은 좌표에 모인 원자 처리
        for (x, y), infos in hash_map.items():
            # 2개 미만인 경우는 충돌 X
            if len(infos) >= 2:
                for _, energy in infos:
                    total += energy
            else:
                # 충돌하지 않은 원자 1개인 경우
                d, k = infos[0]
                if -2000 <= x <= 2000 and -2000 <= y <= 2000:
                    next_atoms.append([x, y, d, k])

        # 살아남은 원자
        atoms = next_atoms

    print(f"#{tc} {total}")