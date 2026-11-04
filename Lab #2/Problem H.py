import sys

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    values = [int(x) for x in input_data[1:n+1]]

    head = Node(values[0])
    curr = head
    for i in range(1,n):
        curr.next = Node(values[i])
        curr = curr.next
    
    max_so_far = head.val
    current_max = head.val

    curr = head.next
    while curr:
        current_max = max(curr.val, current_max+curr.val)
        max_so_far = max(max_so_far, current_max)
        curr = curr.next

    print(max_so_far)

if __name__ == "__main__":
    solve()