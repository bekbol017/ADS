import sys, heapq

data = sys.stdin.read().split()
n, x = int(data[0]), int(data[1])
h = [-int(v) for v in data[2:2+n]]
heapq.heapify(h)

ttl = 0
for _ in range(x):
    k = -h[0]
    ttl += k
    if k>1:
        heapq.heapreplace(h, -(k-1))
    else:
        heapq.heappop(h)

print(ttl)