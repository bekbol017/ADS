import sys

def solve():
    inp_d = sys.stdin.read().split()
    if not inp_d:
        return
    
    N = int(inp_d[0])
    H = int(inp_d[1])

    bags = [int(x) for x in inp_d[2:2+N]]

    def check(K):
        h = 0
        for b in bags:
            h += (b+K-1) // K
            if h>H:
                return False
        return h<=H

    low = 1
    high = max(bags)
    ans = high

    while low<=high:
        mid = (low+high) //2
        if check(mid):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    
    print(ans)

if __name__ == "__main__":
    solve()