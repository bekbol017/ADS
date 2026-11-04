import sys

def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2+n]))

    def ok(M):
        blocks=1
        cur=0
        for x in a:
            if cur+x>M:
                blocks +=1
                if blocks >k:
                    return False
                cur = x
            else:
                cur += x
        return True

    lo, hi = max(a), sum(a)
    while lo < hi:
        mid = (lo+hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid+1
    print(lo)

main()