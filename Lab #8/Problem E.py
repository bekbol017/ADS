import sys
def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    suffixes = sorted(s[i:] for i in range(n))
    def lcp(a,b):
        lo, hi = 0, min(len(a), len(b))
        while lo<hi:
            mid = (lo+hi+1)//2
            if a[:mid] == b[:mid]:
                lo = mid
            else:
                hi = mid-1
        return lo

    ans = n*(n+1)//2
    for i in range(1,n):
        ans -= lcp(suffixes[i-1], suffixes[i])
    
    print(ans)

main()