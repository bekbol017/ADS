import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    pos = 0
    out = []
    while True:
        n = int(data[pos]); pos+=1
        if n == 0:
            break
        pats = data[pos:pos+n]; pos+=n
        text = data[pos]; pos+=1

        go = [[-1]*26]
        ends = []
        for p in pats:
            cur = 0
            for ch in p:
                c = ord(ch)-97
                if go[cur][c] == -1:
                    go[cur][c] = len(go)
                    go.append([-1]*26)
                cur = go[cur][c]
            ends.append(cur)
        
        fail = [0]*len(go)
        order = []
        q =deque()
        for c in range(26):
            v = go[0][c]
            if v == -1:
                go[0][c] = 0
            else:
                q.append(v)
        while q:
            u = q.popleft()
            order.append(u)
            for c in range(26):
                v = go[u][c]
                if v == -1:
                    go[u][c] = go[fail[u]][c]
                else:
                    fail[v] = go[fail[u]][c]
                    q.append(v)
        cnt = [0]*len(go)
        cur = 0
        for ch in text:
            cur = go[cur][ord(ch)-97]
            cnt[cur] +=1
        for u in reversed(order):
            cnt[fail[u]] += cnt[u]

        best = max(cnt[e] for e in ends)
        out.append(str(best))
        for p, e in zip(pats, ends):
            if cnt[e] == best:
                out.append(p)
    print('\n'.join(out))

main()