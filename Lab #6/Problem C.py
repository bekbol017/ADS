import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = sorted(map(int, data[1:1+n]))

    b = min(a[i+1]-a[i] for i in range(n-1))

    res = []
    for i in range(n-1):
        if a[i+1]-a[i] == b:
            res.append(a[i])
            res.append(a[i+1])

    print(" ".join(map(str, res)))

main()  