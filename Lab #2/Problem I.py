import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    dll = deque()
    idx = 0
    n = len(input_data)
    while idx < n:
        cmd = input_data[idx]
        idx += 1

        if cmd == "add_front":
            title = input_data[idx]
            idx += 1
            dll.appendleft(title)
            print("ok")
        elif cmd == "add_back":
            title = input_data[idx]
            idx += 1
            dll.append(title)
            print("ok")
        elif cmd == "erase_front":
            if not dll:
                print("error")
            else:
                print(dll.popleft())
        elif cmd == "erase_back":
            if not dll:
                print("error")
            else:
                print(dll.pop())
        elif cmd == "front":
            if not dll:
                print("error")
            else:
                print(dll[0])
        elif cmd == "back":
            if not dll:
                print("error")
            else:
                print(dll[-1])
        elif cmd == "clear":
            dll.clear()
            print("ok")
        elif cmd == "exit":
            print("goodbye")
            break

if __name__ == "__main__":
    solve()