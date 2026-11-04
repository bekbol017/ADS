def is_prime(num):
    if num<2:
        return False
    i = 2
    while i*i <= num:
        if num%i == 0:
            return False
        i+=1
    return True

def solve():
    n = int(input())
    count = 0
    current = 2
    while True:
        if is_prime(current):
            count+=1
            if count == n:
                print(current)
                return
        current += 1

if __name__ == "__main__":
    solve()