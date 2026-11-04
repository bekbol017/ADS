import sys

def solve():
    inp_d = sys.stdin.read().split()
    if not inp_d:
        return
    
    n = int(inp_d[0])
    k = int(inp_d[1])

    a = [int(x) for x in inp_d[2:2+n]]
    def check(le):
        if le == 0:
            return True
        cnt = 0
        for x in a:
            cnt += int(x/le)
            if cnt >= k:
                return True
        return cnt >= k

    low = 0.0
    high = float(max(a))

    for _ in range(100):
        mid = (low+high) / 2.0
        if check(mid):
            low = mid
        else:
            high = mid
    
    print(f"{low:.9f}")

if __name__ == "__main__":
    solve()