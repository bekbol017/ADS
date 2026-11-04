import sys, heapq

def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    a = sorted(map(int, data[2:2+n]))
    q = []
    i = j = 0
    cnt = 0
    INF = float('inf')

    while True:
        ai = a[i] if i<n else INF
        qj = q[j] if j<len(q) else INF
        if ai<=qj:
            x = ai; i+=1
        else:
            x = qj; j+=1
        
        if x>=m:
            print(cnt)
            return

        if i>=n and j>=len(q):
            print(-1)
            return
        
        ai = a[i] if i<n else INF
        qj = q[j] if j<len(q) else INF
        if ai<=qj:
            y = ai; i+=1
        else:
            y = qj; j+=1

        q.append(x+2*y)
        cnt += 1

main()