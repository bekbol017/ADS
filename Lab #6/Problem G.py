import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    cur = {}
    pos = 1
    for _ in range(n):
        old, new = data[pos], data[pos+1]
        pos += 2
        orig = cur.pop(old, old) 
        cur[new] = orig

    res = sorted((orig, now) for now, orig in cur.items())
    out = [str(len(res))]
    for orig, now in res:
        out.append(orig + " " + now)
    print('\n'.join(out))       

main()