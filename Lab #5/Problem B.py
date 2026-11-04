import sys,heapq

data = sys.stdin.read().split()
n = int(data[0])
a = [-int(v) for v in data[1:1+n]]

heapq.heapify(a)
while len(a)>1:
    x = -heapq.heappop(a)
    y = -heapq.heappop(a)
    if x!=y:
        heapq.heappush(a,-(x-y))

print(-a[0] if a else 0)