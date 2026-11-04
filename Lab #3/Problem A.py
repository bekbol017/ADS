import sys
def binary_search(arr, x):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] == x:
            return True
        elif arr[mid] <x:
            l = mid+1
        else:
            r = mid-1
    
    return False

def solve():
    inp_d = sys.stdin.read().split()
    if not inp_d:
        return
    n = int(inp_d[0])
    arr = [int(val) for val in inp_d[1:1+n]]
    x = int(inp_d[1+n])

    if binary_search(arr, x):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()