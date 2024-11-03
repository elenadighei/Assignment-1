def Heap(a, n, i):
    largest = i  
    left = 2 * i  
    right = 2 * i + 1  

    if left < n and a[left] > a[largest]:  
        largest = left
    if right < n and a[right] > a[largest]:  
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        Heap(a, n, largest)

def build_max_heap(a):
    n = len(a)

    for i in range(n//2-1 , -1, -1):  
        Heap(a, n, i)

def heap_sort(a):
    n = len(a)
    build_max_heap(a)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        Heap(a, i, 0)

    return a

if __name__ == "__main__":
    with open("/home/elenadg04/PoC2/rosalind_hs (4).txt", "r") as file:
        n = int(file.readline().strip()) 
        a = list(map(int, file.readline().strip().split()))

    sorted_array = heap_sort(a)

    with open("/home/elenadg04/PoC2/rosalind_hs_output (6).txt", "w") as file:
        file.write(" ".join(map(str, sorted_array)))