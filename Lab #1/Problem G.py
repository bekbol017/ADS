def solve():
    s = input().strip()
    st = []

    for char in s:
        if st and st[-1] == char:
            st.pop()
        else:
            st.append(char)
    if not st:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()