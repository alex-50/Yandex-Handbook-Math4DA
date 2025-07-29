import sys

matrix = [
    list(map(int, string.strip().split())) for string in sys.stdin.readlines()
]

loops_indexes = [i for i in range(len(matrix)) if matrix[i][i]]

print("\n".join(map(str, loops_indexes)) if loops_indexes else "NO LOOPS")
