import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    boris = deque(map(int, input_data[:5]))
    nursik = deque(map(int, input_data[5:10]))
    
    moves = 0
    
    while boris and nursik:
        moves += 1
        
        c_boris = boris.popleft()
        c_nursik = nursik.popleft()
        
        if c_boris == 0 and c_nursik == 9:
            boris_wins = True
        elif c_boris == 9 and c_nursik == 0:
            boris_wins = False
        else:
            boris_wins = c_boris > c_nursik
            
        if boris_wins:
            boris.append(c_boris)
            boris.append(c_nursik)
        else:
            nursik.append(c_boris)
            nursik.append(c_nursik)
            
    if boris:
        print(f"Boris {moves}")
    else:
        print(f"Nursik {moves}")

if __name__ == "__main__":
    solve()