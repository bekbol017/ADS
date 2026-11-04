import sys

def main():
    data = sys.stdin.readline().strip()

    cnt = [0] *26
    for ch in data:
        cnt[ord(ch) - 97] += 1

    res =[]
    for i in range(26):
        res.append(chr(97+i) * cnt[i])

    print("".join(res))

main()