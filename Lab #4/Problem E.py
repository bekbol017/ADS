import sys
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    chil = [[] for _ in range(n+1)]
    idx = 1
    for _ in range(n-1):
        x = int(data[idx])
        y = int(data[idx+1])
        idx+=3
        chil[x].append(y)

    level = [1]
    best = 1
    while level:
        best = max(best,  len(level))
        nxt = []
        for u in level:
            nxt.extend(chil[u])
        level = nxt
    print(best)

main()