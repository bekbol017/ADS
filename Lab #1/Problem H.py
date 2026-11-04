def solve():
    n = int(input())
    a = list(map(int, input().split()))

    st = []
    ans = []

    for x in a:
        
        while st and st[-1] >= x:
            st.pop()

        
        if st:
            ans.append(st[-1])
        else:
            ans.append(-1)

        
        st.append(x)

    print(*ans)

if __name__ == "__main__":
    solve()