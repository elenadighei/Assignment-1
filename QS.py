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
    arr = QS(smaller) + [pivot] + QS(larger)   
    return arr

if __name__ == '__main__':
    with open('/home/elenadg04/PoC2/rosalind_qs (1).txt', "r") as f:
        n = int(f.readline().strip()) 
        a = list(map(int, f.readline().strip().split()))  
        
result = QS(a)
with open('/home/elenadg04/PoC2/rosalind_qs_output (1).txt', 'w') as f:
            f.write(' '.join(map(str, result)))

