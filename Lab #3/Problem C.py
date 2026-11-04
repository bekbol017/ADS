import sys
import bisect

def solve():
    inp_d = sys.stdin.read().split()
    if not inp_d:
        return

    N = int(inp_d[0])
    M = int(inp_d[1])

    a = [int(x) for x in inp_d[2:2+N]]

    prev = [0] * N
    prev[0] = a[0]
    for i in range(1,N):
        prev[i] = prev[i-1] + a[i]

    out = []
    idx = 2+N
    for _ in range(M):
        b = int(inp_d[idx])
        idx += 1

        bl_idx = bisect.bisect_left(prev, b)
        out.append(str(bl_idx+1))
    
    print("\n".join(out))

if __name__ == "__main__":
    solve()