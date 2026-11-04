import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0]
    q = int(data[1])

    cache = {}
    out = []
    idx = 2
    for _ in range(q):
        l = int(data[idx])
        r = int(data[idx+1])
        idx+=2
        sub = s[l-1:r]
        if sub in cache:
            out.append(str(cache[sub]))
        else:
            cnt = 0
            pos = s.find(sub)
            while pos!=-1:
                cnt+=1
                pos = s.find(sub,pos+1)
            cache[sub] = cnt
            out.append(str(cnt))
    print('\n'.join(out))

main()