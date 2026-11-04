import sys
import bisect

def solve():
    inp_d = sys.stdin.read().split()
    if not inp_d:
        return

    n = int(inp_d[0])
    q = int(inp_d[1])

    a = [int(x) for x in inp_d[2:2+n]]
    a.sort()

    idx = 2+n
    out = []

    def cnt_in_r(l,r):
        if l>r:
            return 0
        l_idx = bisect.bisect_left(a, l)
        r_idx = bisect.bisect_right(a, r)
        return r_idx - l_idx

    for _ in range(q):
        l1 = int(inp_d[idx])
        r1 = int(inp_d[idx+1])
        l2 = int(inp_d[idx+2])
        r2 = int(inp_d[idx+3])
        idx+=4

        cnt_A = cnt_in_r(l1,r1)
        cnt_B = cnt_in_r(l2,r2)

        int_l = max(l1,l2)
        int_r = min(r1,r2)
        cnt_int = cnt_in_r(int_l,int_r)

        ans = cnt_A + cnt_B - cnt_int
        out.append(str(ans))
    print("\n".join(out))

if __name__ == "__main__":
    solve()