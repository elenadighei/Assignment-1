def Sort(a):
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
    arr = Sort(smaller) + [pivot] + Sort(larger)   
    return arr

if __name__ == '__main__':
    with open('/home/elenadg04/PoC2/rosalind_med (2).txt', "r") as f:
        n = int(f.readline().strip()) 
        a = list(map(int, f.readline().strip().split()))  
        k = int(f.readline().strip())

sorted_arr = Sort(a)

def Med(sorted_arr, k):
    index = (k - 1)

    if 0 <= index < len(sorted_arr):
        return sorted_arr[index]
    else:
        return None 
    
result = Med(sorted_arr, k)
with open('/home/elenadg04/PoC2/rosalind_med_output (1).txt', 'w') as f:
            f.write(str(result))
    




