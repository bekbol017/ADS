import sys

def main():
    data = sys.stdin.read().split()
    n , k = int(data[0]), int(data[1])
    a = list(map(int, data[2:2+n]))

    s=0
    l=0
    ans = n
    for r in range(n):
        s+=a[r]
        while l<=r and s>=k:
            ans = min(ans,r-l+1)
            s-=a[l]
            l+=1
    
    print(ans)

main()