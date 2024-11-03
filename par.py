def Part(a):
    pivot = a[0]
    smaller = []
    larger = []

    for i in range(1, len(a)):
        if a[i] <= pivot:
            smaller.append(a[i])
        else:
            larger.append(a[i])

    return smaller + [pivot] + larger        


if __name__ == '__main__':
    with open('/home/elenadg04/PoC2/rosalind_par (5).txt', "r") as f:
        n = int(f.readline())
        a = [int(i) for i in f.readline().strip().split(' ')]
b = Part(a)

# output gets truncated in the terminal, so  I write the output in a file txt
with open('/home/elenadg04/PoC2/rosalind_par_output (3).txt', "w") as output_file:
        output_file.write(" ".join(map(str, b)))

