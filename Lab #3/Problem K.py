import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])

    q = [int(x) for x in data[1:1+t]]

    idx = 1+t
    n = int(data[idx])
    m = int(data[idx+1])
    idx+=2

    pos = {}
    for r in range(n):
        for c in range(m):
            val = int(data[idx])
            pos[val] = (r, c)
            idx+=1
    
    out = []
    for d in q:
        if d in pos:
            r, c = pos[d]
            out.append(f"{r} {c}")
        else:
            out.append("-1")

    print('\n'.join(out))

if __name__ == "__main__":
    solve()