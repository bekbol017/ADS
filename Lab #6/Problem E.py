import sys

def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    val = list(map(int, data[2:2+n*m]))

    rs = [val[i*m:(i+1)*m] for i in range(n)]
    cs = [sorted((rs[i][j] for i in range(n)), reverse = True) for j in range(m)]

    out = []
    for i in range(n):
        out.append(" ".join(str(cs[j][i]) for j in range(m)))
    print('\n'.join(out))

main()