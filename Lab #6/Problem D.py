import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    dates = data[1:1+n]

    def key(s):
        d,m,y = s.split("-")
        return (int(y), int(m), int(d))

    dates.sort(key=key)
    print('\n'.join(dates))

main()