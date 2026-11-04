import sys
def solve():
    data_input = sys.stdin.read().split()
    a = int(data_input[0])
    if a<2:
        print("NO")
        return
    i = 2
    while i*i <= a:
        if a%i == 0:
            print("NO")
            return
        i+=1
    print("YES")

if __name__ == "__main__":
    solve()