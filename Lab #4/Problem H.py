import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = sorted(map(int, data[1:1+n]))

    res = []
    s= 0

    for v in reversed(a):
        s+=v
        res.append(s)

    res.sort()
    print(" ".join(map(str, res)))

main()