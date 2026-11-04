import sys

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_length(head):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return length

def insert_node(head, x, p):
    new_node = Node(x)
    if p == 0:
        new_node.next = head
        return new_node
    curr = head
    for _ in range(p-1):
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head

def remove_node(head, p):
    if not head:
        return head, None
    if p == 0:
        val = head.val
        return head.next, val
    curr = head
    for _ in range(p-1):
        curr = curr.next
    val = curr.next.val
    curr.next = curr.next.next
    return head, val

def print_list(head):
    if not head:
        print(-1)
        return
    res = []
    curr = head
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(" ".join(res))

def replace_node(head, p1, p2):
    head, val = remove_node(head, p1)
    head = insert_node(head, val, p2)
    return head

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr= nxt
    return prev

def cyclic_left(head, x):
    n = get_length(head)
    if n <= 1:
        return head
    x = x%n
    if x == 0:
        return head
    
    tail = head
    while tail.next:
        tail = tail.next

    kth = head
    for _ in range(x-1):
        kth = kth.next

    new_head = kth.next
    kth.next = None
    tail.next = head
    return new_head

def cyclic_right(head, x):
    n = get_length(head)
    if n <= 1:
        return head
    x = x%n
    if x == 0:
        return head
    return cyclic_left(head, n-x)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    head = None

    while idx < len(input_data):
        cmd = int(input_data[idx])
        idx +=1

        if cmd == 0:
            break
        elif cmd == 1:
            x = int(input_data[idx])
            p = int(input_data[idx+1])
            idx +=2
            head = insert_node(head, x, p)
        elif cmd == 2:
            p = int(input_data[idx])
            idx += 1
            head, _ = remove_node(head,p)
        elif cmd == 3:
            print_list(head)
        elif cmd == 4:
            p1 = int(input_data[idx])
            p2 = int(input_data[idx+1])
            idx += 2
            head = replace_node(head, p1, p2)
        elif cmd == 5:
            head = reverse_list(head)
        elif cmd == 6:
            x = int(input_data[idx])
            idx+=1
            head = cyclic_left(head,x)
        elif cmd == 7:
            x = int(input_data[idx])
            idx+=1
            head = cyclic_right(head, x)

if __name__ == "__main__":
    solve()
