import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))

    pos = [0] * (n+2)
    for i,  v in enumerate(a):
        pos[v] = i+1

    cnt = 0
    for v in range(2, n):
        if pos[v-1]>pos[v] and pos[v+1] > pos[v]:

            cnt+=1
    print(cnt)
main()