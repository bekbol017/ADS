import sys
class Node:
    def __init__(self, val="", next=None):
        self.val = val
        self.next = next

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    words = input_data[2:n+2]

    head = Node(words[0])
    curr = head
    for i in range(1, n):
        curr.next = Node(words[i])
        curr = curr.next

    tail = curr

    kth_node = head
    for _ in range(k-1):
        kth_node = kth_node.next

    tail.next = head
    head = kth_node.next
    kth_node.next = None

    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next

    print(" ".join(res))

if __name__ == "__main__":
    solve()