import sys
from collections import Counter

def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    a = data[2:2+n]
    b = data[2+n:2+n+m]

    ca = Counter(map(int, a))
    cb = Counter(map(int, b))

    res = []
    for x in sorted(ca.keys() & cb.keys()):
        res.extend([x] * min(ca[x], cb[x]))

    print(" ".join(map(str, res)))

main()