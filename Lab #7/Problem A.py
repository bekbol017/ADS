import sys
def main():
    data = sys.stdin.read().split('\n')
    t = int(data[0])
    out = []
    for i in range(1,t+1):
        w = data[i].split()
        w.sort(key=len)
        out.append(' '.join(w))
    print('\n'.join(out))
main()