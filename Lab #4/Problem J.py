import sys

def main():
    data = sys.stdin.read().split()
    n , k = int(data[0]),  int(data[1])
    a= sorted(map(int, data[2:2+n]))

    if k>n:
        print(-1)
    else:
        print(a[k-1])
main()