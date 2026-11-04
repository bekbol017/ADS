import sys
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    p = list(map(int, data[1:1+n]))
    pos = [0] * (n+2)
    for i,v in enumerate(p):
        pos[v] = i+1
    cnt = 0
    for v in range(1,n+1):
        h_left = v>1 and pos[v-1] > pos[v]
        h_right = v < n and pos[v+1] > pos[v]
        if not h_left and not h_right:
            cnt+=1
    print(cnt)
main()