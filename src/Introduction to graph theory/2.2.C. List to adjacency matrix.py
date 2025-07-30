N = int(input())

for i in range(N):
    row = [0] * N

    if buf := input():
        for v_index in map(int, buf.split()):
            row[v_index] = 1

    print(*row)
