import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    names = input_data[1:n+1]
    result = []
    last_name = None

    for name in names:
        if name != last_name:
            result.append(name)
            last_name = name

    print(len(result))
    print("\n".join(result))

if __name__ == "__main__":
    solve()