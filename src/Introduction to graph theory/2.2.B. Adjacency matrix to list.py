import sys

for string in sys.stdin.readlines():
    indexes = [i for i, w in enumerate(map(int, string.strip().split())) if int(w)]
    print(*indexes)
