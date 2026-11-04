import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    p = list(map(int, data[1:1+n]))

    prev = list(range(-1, n+1))
    nxt = list(range(1, n+3))
    pr = [0] * (n+2)
    nx = [0] * (n+2)

    for i in range(n-1, -1, -1):
        v = p[i]
        a = prev[v]
        b = nxt[v]
        pr[v] = a
        nx[v] = b
        nxt[a] = b
        prev[b] = a

    depth = [-1] * (n+2)
    sums = []
    for v in p:
        d = max(depth[pr[v]], depth[nx[v]]) + 1
        depth[v] = d
        if d == len(sums):
            sums.append(0)
        sums[d] += v

    print(len(sums))
    print(" ".join(map(str, sums)))

main()