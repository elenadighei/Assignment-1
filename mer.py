def Merge(a, b):
    c = []
    i = 0
    j= 0

    
    while i<n and j<m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:]
    c += b[j:]
    return c

if __name__ == '__main__':
    with open('/home/elenadg04/PoC2/rosalind_mer (11).txt', "r") as f:
        n = int(f.readline())
        a = [int(i) for i in f.readline().strip().split(' ')]
        m = int(f.readline())
        b = [int(i) for i in f.readline().strip().split(' ')]
    c = Merge(a, b)
    for i in c:
        print(i, end=" ")
    print()





