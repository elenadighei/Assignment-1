def Heap(a, n, i):
    largest = i  
    left = 2 * i  
    right = 2 * i + 1  

    if left <= n and a[left - 1] > a[largest - 1]:  
        largest = left

    
    if right <= n and a[right - 1] > a[largest - 1]:  
        largest = right

    
    if largest != i:
        a[i - 1], a[largest - 1] = a[largest - 1], a[i - 1]
        Heap(a, n, largest)

def build_max_heap(a):
    n = len(a)
    for i in range(n//2, 0, -1):  
        Heap(a, n, i)
    return a

with open('/home/elenadg04/PoC2/rosalind_hea (1).txt', 'r') as infile:
    n = int(infile.readline().strip())  
    a = list(map(int, infile.readline().strip().split()))  

result = build_max_heap(a)


with open('/home/elenadg04/PoC2/rosalind_hea_output (1).txt', 'w') as outfile:
    outfile.write(' '.join(map(str, result)) + '\n')

