import sys

def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    rows = []
    pos = 2
    for i in range(n):
        rows.append(list(map(int, data[pos:pos+m])))
        pos+=m

    rows.sort(key=lambda r: (-sum(r), r))

    print('\n'.join(" ".join(map(str, r)) for r in rows))

main()