import sys
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    
    return dummy.next

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0

    n = int(input_data[idx])
    idx += 1

    head1 = None
    if n>0:
        head1 = Node(int(input_data[idx]))
        curr = head1
        idx+=1
        for _ in range(1, n):
            curr.next = Node(int(input_data[idx]))
            curr = curr.next
            idx += 1
    m = int(input_data[idx])
    idx += 1

    head2 = None
    if m>0:
        head2 = Node(int(input_data[idx]))
        curr = head2
        idx += 1
        for _ in range(1,m):
            curr.next = Node(int(input_data[idx]))
            curr = curr.next
            idx += 1

    merged_head = merge_two_lists(head1, head2)

    result = []
    curr = merged_head
    while curr:
        result.append(str(curr.val))
        curr = curr.next
    print(" ".join(result))

if __name__ == "__main__":
    solve()