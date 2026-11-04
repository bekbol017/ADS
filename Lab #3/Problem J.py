import sys

def main():
    data =sys.stdin.buffer.read().split()
    n , k = int(data[0]), int(data[1])
    costs = []
    idx = 2
    for _ in range(n):
        x2 = int(data[idx+2])
        y2 = int(data[idx+3])
        costs.append(x2 if x2>y2 else y2)
        idx+=4
    costs.sort()
    print(costs[k-1])

main()