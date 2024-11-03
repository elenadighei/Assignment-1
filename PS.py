def QS(a):
    if len(a) <= 1:
        return a
    
    pivot = a[0]
    smaller = []
    larger = []
    for i in range(1, len(a)):
        if a[i] <= pivot:
            smaller.append(a[i])
        else:
            larger.append(a[i])
    return QS(smaller) + [pivot] + QS(larger)   
    


def Part_Sort(a, k):
    sorted_a = QS(a)
    b = []
    for i in range(k):
        b.append(sorted_a[i])
    
    return b


if __name__ == "__main__":
    with open("/home/elenadg04/PoC2/rosalind_ps (1).txt", "r") as file:
        n = int(file.readline().strip()) 
        a = list(map(int, file.readline().strip().split()))
        k = int(file.readline().strip())

    result = Part_Sort(a, k)

    with open("/home/elenadg04/PoC2/rosalind_ps_output (1).txt", "w") as file:
        file.write(" ".join(map(str, result)))





