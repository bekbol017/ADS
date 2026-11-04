import sys, heapq

def main():
    data = sys.stdin.read().split()
    q, k = int(data[0]), int(data[1])
    h = []
    s = 0
    out = []
    p = 2
    for _ in range(q):
        cmd = data[p]; p+=1
        if cmd == "insert":
            v = int(data[p]); p+=1
            if len(h) < k:
                heapq.heappush(h, v)
                s += v
            elif v>h[0]:
                s+=v-heapq.heapreplace(h, v)
        else:
            out.append(s)
    print('\n'.join(map(str, out)))

main()