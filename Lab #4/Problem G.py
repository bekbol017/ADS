import sys
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = data[1:1+n]

    seen = set()
    order = []
    for s in a:
        v = int(s)
        if v not in seen:
            seen.add(v)
            order.append(v)
    m = len(order)
    sv = sorted(order)
    rank = {v: i+1 for i, v in enumerate(sv)}
    ranks = [rank[v] for v in order]

    t = [-1] * (m+2)
    for i, r in enumerate(ranks):
        t[r] = i

    prev = list(range(-1,m+1))
    nxt = list(range(1,m+3))
    par = [0] * (m+2)

    for i in range(m-1,-1,-1):
        r = ranks[i]
        x = prev[r]
        y = nxt[r]
        if t[x] == -1 and t[y] == -1:
            par[r] = 0
        elif t[x] >t[y]:
            par[r] = x
        else:
            par[r] = y
        nxt[x] = y
        prev[y] = x
    hl = [0] * (m+2)
    hr = [0] * (m+2)
    diam = 1
    for i in range(m-1,-1,-1):
        r = ranks[i]
        h = 1+max(hl[r], hr[r])
        d = hl[r] + hr[r]+1
        if d>diam:
            diam = d
        p = par[r]
        if p:
            if p<r:
                hr[p]= h
            else:
                hl[p] = h
    print(diam)
main()