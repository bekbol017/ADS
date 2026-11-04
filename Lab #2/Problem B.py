import sys

class Node:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    values = input_data[1:n+1]

    if n== 0 :
        return

    head = Node(int(values[0]))
    curr = head
    for i in range(1, n):
        curr.next = Node(int(values[i]))
        curr = curr.next

    curr = head
    while curr and curr.next:
        curr.next = curr.next.next
        curr = curr.next

    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.next

    print(" ".join(result))

if __name__ == "__main__":
    solve()