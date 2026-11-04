import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    res = []

    for idx in range(1, t + 1):
        n = int(input_data[idx])
        dq = deque()

        for i in range(n, 0, -1):
            dq.appendleft(i)
            dq.rotate(i)

        res.append(" ".join(map(str, dq)))

    sys.stdout.write("\n".join(res) + "\n")

if __name__ == "__main__":
    solve()