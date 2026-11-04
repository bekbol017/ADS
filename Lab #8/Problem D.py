import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    p = [int(x) for x in data[1:]]

    res = [chr(p[0]+97)]

    for i in range(1,N):
        diff = p[i]-p[i-1]
        val = diff//(1<<i)
        char = val+97
        res.append(chr(char))

    print("".join(res))

main()