import sys
import bisect

def solve():
    inp_d = sys.stdin.read().split()
    if not inp_d:
        return

    N = int(inp_d[0])
    a = [int(x) for x in inp_d[1:1+N]]

    a.sort()

    pref = [0] * (N+1)
    for i in range(N):
        pref[i+1] = pref[i] + a[i]

    P = int(inp_d[1+N])
    out = []
    idx = 2+N

    for _ in range(P):
        p_i = int(inp_d[idx])
        idx += 1

        cnt = bisect.bisect_right(a, p_i)
        ttl_sum = pref[cnt]

        out.append(f"{cnt} {ttl_sum}")

    print('\n'.join(out))

if __name__ == "__main__":
    solve()