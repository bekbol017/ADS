import sys
from collections import deque, Counter

def solve():
    input = sys.stdin.read
    data = input().split()

    if not data:
        return
    
    t = int(data[0])
    idx = 1
    output = []
    for _ in range(t):
        n = int(data[idx])
        stream = data[idx+1:idx+1+n]
        idx+=1+n

        freq = Counter()
        q = deque()
        res = []

        for char in stream:
            freq[char] += 1
            q.append(char)

            while q and freq[q[0]] > 1:
                q.popleft()

            if not q:
                res.append("-1")
            else:
                res.append(q[0])
        output.append(" ".join(res))
    print("\n".join(output))

if __name__ == "__main__":
    solve()