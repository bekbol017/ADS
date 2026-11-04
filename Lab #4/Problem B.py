import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    x = int(data[1+n])

    val = [a[0]]
    L = [-1]
    R = [-1]

    for v in a[1:]:
        cur = 0
        while True:
            if v < val[cur]:
                if L[cur] == -1:
                    val.append(v)
                    L.append(-1)
                    R.append(-1)
                    L[cur] = len(val) - 1
                    break
                cur = L[cur]

            else:
                if R[cur] == -1:
                    val.append(v)
                    L.append(-1)
                    R.append(-1)
                    R[cur] = len(val) - 1
                    break
                cur = R[cur]


    start = val.index(x)
    st = [start]
    cnt = 0
    while st:
        u = st.pop()
        cnt += 1
        if L[u] != -1:
            st.append(L[u])
        if R[u] != -1:
            st.append(R[u])
    
    print(cnt)

main()