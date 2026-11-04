import sys
def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    a = data[2:2+n]
    paths = data[2+n:2+n+m]

    MAXD = 100
    val = [int(a[0])]
    L = [-1]
    R = [-1]

    for i in range(1,n):
        v = int(a[i])
        cur = 0
        depth = 0
        while True:
            depth += 1
            if v <= val[cur]:
                nxt = L[cur]
                if nxt == -1:
                    if depth <= MAXD:
                        val.append(v)
                        L.append(-1)
                        R.append(-1)
                        L[cur] = len(val) - 1
                    break
            else:
                nxt = R[cur]
                if nxt == -1:
                    if depth <= MAXD:
                        val.append(v)
                        L.append(-1)
                        R.append(-1)
                        R[cur] = len(val) - 1
                    break
            cur = nxt
    out = []
    for p in paths:
        cur = 0
        ok = True
        for ch in p:
            cur = L[cur] if ch == "L" else R[cur]
            if cur == -1:
                ok = False
                break
        out.append("YES" if ok else "NO")
    print("\n".join(out))

main()