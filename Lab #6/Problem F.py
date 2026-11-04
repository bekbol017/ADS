import sys

def main():
    data = sys.stdin.read().split()
    scale = {"A+": 4.0, "A": 3.75, "B+": 3.5, "B": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0}

    n = int(data[0])
    pos = 1
    sts = []
    for _ in range(n):
        l = data[pos]
        f = data[pos+1]
        m = int(data[pos+2])
        pos += 3
        num = 0.0
        den = 0
        for _ in range(m):
            g = scale[data[pos]]
            c = int(data[pos+1])
            pos += 2
            num += g*c
            den += c
        gpa = num/den
        sts.append((gpa, l, f))

    sts.sort()
    out = ["%s %s %.3f" % (l, f, gpa) for gpa, l, f in sts]
    print('\n'.join(out))
main()