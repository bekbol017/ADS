a,b,t = open(0).read().split()
M = 2**61-1
B = 911382323
n = len(t)
P = pow(B,n,M)
T = 0
for c in t.encode():
    T = (T*B+c)%M
def f(s):
    s=s.encode()
    h=0
    r = []
    for x,y in zip(s,bytes(n)+s):
        h = (h*B+x-y*P)%M
        r.append(h==T)
    return r
print(sum(x&y for x,y in zip(f(a),f(b))))