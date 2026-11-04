import sys
from bisect import bisect_right

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = data[1:1+n]
    k = data[1+n]

    i = bisect_right(arr, k)
    print(arr[i] if i<n else arr[0])

main()