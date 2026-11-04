def process(s):
    res = []
    for char in s:
        if char == "#":
            if res:
                res.pop()
        else:
            res.append(char)
    return res 

s1 = input()
s2 = input()
if process(s1) == process(s2):
    print("Yes")
else:
    print("No")