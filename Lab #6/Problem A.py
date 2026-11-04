n = int(input())
s = input().strip()

v = "aeiou"
cnt = [0]*26
for ch in s:
    cnt[ord(ch)-97] += 1

res = []
for a in v:
    res.append(a*cnt[ord(a)-97])
for i in range(26):
    c = chr(97+i)
    if c not in v:
        res.append(c*cnt[i])

print("".join(res))