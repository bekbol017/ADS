import math
import sys

def solve():
    a, b = map(int, input().split())
    print(math.gcd(a, b))

if __name__ == "__main__":
    solve()