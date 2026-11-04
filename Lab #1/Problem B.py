import sys
import math

def solve():
    data_input = sys.stdin.read().split()
    if not data_input:
        return
    a = int(data_input[0])
    b = int(data_input[1])
    c = int(data_input[2])
    print(pow(a,b,c))

if __name__ == "__main__":
    solve()