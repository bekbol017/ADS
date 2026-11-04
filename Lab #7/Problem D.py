import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))

    def s_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        l, c1 = s_count(arr[:mid])
        r, c2 = s_count(arr[mid:])
        merged = []
        i = j = 0
        cnt = c1+c2
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                merged.append(l[i]); i+=1
            else:
                merged.append(r[j]); j+=1
                cnt += len(l) - i
        merged.extend(l[i:])
        merged.extend(r[j:])
        return merged, cnt

    print(s_count(a)[1])

main()